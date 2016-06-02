from rest_framework import viewsets
from .models import InterestGroup, Post, Membership, MemberShipRequest
from .serializers import InterestGroupSerializer, PostSerializer, MemberShipRequestSerializer, MemberShipSerializer
from django.views.generic import DetailView, CreateView
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import UpdateView
from django.http.response import HttpResponseRedirect, HttpResponseServerError

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import MemberShipRequestForm
from django.core.urlresolvers import reverse
from django.contrib import messages

from apps.userProfile.models import UserProfile

from rest_framework.exceptions import PermissionDenied
from django.db.models import Q

from rest_framework.decorators import permission_classes
from rest_framework.permissions import SAFE_METHODS


class IsOwner(BasePermission):
    """
    Permission to check if a user is owner group
    """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsOwnerGroup(BasePermission):
    """
        Permission to check if the user can access this information to group
    """
    def has_permission(self, request, view):
        group_pk = request.query_params.get('group')
        try:
            group = InterestGroup.objects.get(pk=group_pk)
            return group.owner == request.user
        except InterestGroup.DoesNotExist:
            pass

        return False


class MemberShipViewSet(viewsets.ModelViewSet):
    serializer_class = MemberShipSerializer
    permission_classes = (IsOwnerGroup,)

    def get_queryset(self):
        group_pk = self.request.query_params.get('group')

        return Membership.objects.filter(group=group_pk)

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class MemberShipRequestViewSet(viewsets.ModelViewSet):
    serializer_class = MemberShipRequestSerializer
    permission_classes = (IsOwnerGroup,)

    def get_queryset(self):
        group_pk = self.request.query_params.get('group')
        return MemberShipRequest.objects.filter(group=group_pk, status=0) #.exclude(status__in=[3, 4])

    @list_route(methods=['post'])
    def invite_member(self, request, *args, **kwargs):
        email = request.data.get('email')
        group_pk = self.request.query_params.get('group')

        if not email:
            return Response({"errors": {'email': ['This field is required']}},
                            status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     try:
        #         validate_email(email)
        #     except ValidationError:
        #         return Response({"errors": {'email': ['Email format error']}},
        #                     status=status.HTTP_400_BAD_REQUEST)

        if not group_pk:
            return Response({"errors": {'group': ['The param group is required']}},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            group = InterestGroup.objects.get(pk=group_pk)
            membership_request = MemberShipRequest()
            membership_request.email = email
            membership_request.group = group
            membership_request.status = 1
            membership_request.save()
        except InterestGroup.DoesNotExist:
            return Response({"errors": {'group': ['The group pk not found']}},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Success, invite send"}, status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def confirm_request(self, request, *args, **kwargs):
        membership_request_status = request.data.get('status')

        membership_request = self.get_object()
        if membership_request_status == 2:
            membership_request.accept()
        elif membership_request_status == 3:
            membership_request.reject()
        else:
            return Response({'errors': {'status': ['Error choice status']}},
                        status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': ['success, %s member to this group' % membership_request.get_status_display()]},
                        status=status.HTTP_200_OK)


class InterestGroupViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    queryset = InterestGroup.objects.filter(status=0).exclude(slug='public')
    serializer_class = InterestGroupSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Q(memberships__user=self.request.user) | Q(owner=self.request.user))

    def destroy(self, request, *args, **kwargs):
        group = self.get_object()
        group.status = 1
        group.save()
        return Response({'message': ['success, remove group' ]},
                        status=status.HTTP_200_OK)

    # @detail_route(methods=['get'], permission_classes=[IsOwner])
    # def members(self, request, pk=None):
    #     return super(InterestGroupViewSet, self).retrieve(request, pk=pk)
    #
    # @detail_route(methods=['post'], permission_classes=[IsOwner])
    # def invite(self, request, *args, **kwargs):
    #     email = request.data.get('email')
    #     if not email:
    #         return Response({'fields_errors': [{'email': ['This field is required']}]},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    #     suscription = MemberShipRequest()
    #
    #     suscription.create(email=email, group=self.get_object())
    #     return Response({'message': ['success, invite member to this group']},
    #                     status=status.HTTP_202_ACCEPTED)
    #
    # @detail_route(methods=['delete'], permission_classes=[IsOwner])
    # def remove_member(self, request, *args, **kwargs):
    #     profile_pk = request.query_params.get('user')
    #     if not profile_pk:
    #         return Response({'fields_errors': [{'user': ['This field is required']}]},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #     try:
    #         profile = UserProfile.objects.get(pk=profile_pk)
    #         profile.interest_groups.remove(self.get_object())
    #         profile.save()
    #     except UserProfile.DoesNotExist:
    #         return Response({'fields_errors': [{'user': ['This fields not belong to a member']}]},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    #     return Response({'message': ['success, remove member to this group']},
    #                     status=status.HTTP_202_ACCEPTED)





class IsGroupOwnerOrMemberReadOnly(BasePermission):

    def has_permission(self, request, view):
        group_pk = request.query_params.get('group')
        try:
            group = InterestGroup.objects.get(pk=group_pk)

            if request.user and request.user == group.owner:
                return True
            else:
                return request.method in SAFE_METHODS and Membership.objects.get(user=request.user, group=group)
        except InterestGroup.DoesNotExist:
            pass
        except Membership.DoesNotExist:
            pass

        return False

    def has_object_permission(self, request, view, obj):
        return obj.group.owner == request.user


class PostViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsGroupOwnerOrMemberReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        group_pk = self.request.query_params.get('group')
        if not group_pk:
            #raise ValidationError('The param group is required')
            # TODO: Return validation to the param is required
            return []
        return Post.objects.filter(group__pk=group_pk)




class InterestGroupDetail(DetailView):
    template_name = "interest_group/details.html"
    model = InterestGroup
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super(InterestGroupDetail, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['subscription'] = MemberShipRequest.objects.filter(group=self.object, user=self.request.user)
        else:
            context['subscription'] = None

        return context


class InvitationGroup(UpdateView):
    """
        This view execute when user accept invitation to join group.
        Is required the user is authenticate
    """
    template_name = 'interest_group/invitation.html'
    model = MemberShipRequest
    form_class = MemberShipRequestForm
    queryset = MemberShipRequest.objects.filter(status=1)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(InvitationGroup, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            return self.queryset.get(hash_invitation=self.kwargs.get('hash'),
                                     group=self.kwargs.get('group_id'))
        except MemberShipRequest.DoesNotExist:
            return None

    def form_valid(self, form):
        response = super(InvitationGroup, self).form_valid(form)

        membership_request = form.clean()
        if membership_request.get('status') == '2':
            messages.success(self.request, "En hora buena! Disfrute de su nuevo grupo.")
        else:
            self.success_url = '/'
            messages.info(self.request, "Disculpe las molestias, ha rechazado la invitacion al grupo correctamente.")
        return response

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        else:
            return reverse('group:detail', kwargs={ 'slug':self.object.group.slug})


    def get_context_data(self, **kwargs):
        context = super(InvitationGroup, self).get_context_data(**kwargs)
        context['membership_request'] = self.get_object()
        return context

class JoinGroup(CreateView):
    """
        This view execute when the user requested for belong to some group.
        Is required the user is authenticate.
    """
    model = MemberShipRequest

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        try:
            group = InterestGroup.objects.get(pk=self.kwargs.get('group_id'))
            user = self.request.user
            MemberShipRequest(group=group, user=user).save()
            messages.success(self.request, "Te uniste al grupo, espera a que te aprueben la invitacion.")
            if request.GET.get('next_url'):
                return HttpResponseRedirect(request.GET.get('next_url'))
        except InterestGroup.DoesNotExist:
            # El grupo no existe
            return HttpResponseServerError()

        return HttpResponseRedirect('/')
