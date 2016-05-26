from rest_framework import viewsets
from .models import InterestGroup, Post, Suscription
from .serializers import InterestGroupSerializer, PostSerializer, SuscriptionSerializer
from django.views.generic import DetailView, CreateView
from rest_framework.decorators import detail_route
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import UpdateView
from django.http.response import HttpResponseRedirect, Http404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import SuscriptionForm
from django.core.urlresolvers import reverse
from django.contrib import messages


class IsOwner(BasePermission):
    """
    Permission to check if a user is a recipient
    """
    # def has_permission(self, request, view):
    #     return True

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class JoinGroup(CreateView):
    model = Suscription

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        try:
            group = InterestGroup.objects.get(pk=self.kwargs.get('group_id'))
            user = self.request.user
            Suscription(group=group, user=user).save()
            messages.success(self.request, "Te uniste al grupo, espera a que te aprueben la invitacion.")
            if request.GET.get('next_url'):
                return HttpResponseRedirect(request.GET.get('next_url'))
        except InterestGroup.DoesNotExist:
            # El grupo no existe
            return Http404()
        except:
            # TODO: Que pasa aca?
            return Http404()

        return HttpResponseRedirect('/')


class SuscriptionViewSet(viewsets.ModelViewSet):
    model = Suscription
    serializer_class = SuscriptionSerializer

    def get_queryset(self):
        group_pk = self.request.query_params.get('group')
        try:
            group = InterestGroup.objects.get(pk=group_pk)
            if not group.owner == self.request.user:
                return []
        except InterestGroup.DoesNotExist:
            return Response({'errors': {'group': ['The group doesnt exists']}}, status=status.HTTP_400_BAD_REQUEST)
        if group_pk and group:
            return Suscription.objects.filter(group=group_pk).exclude(status__in=[3, 4])
        else:
            return Response({'errors': {'group': ['This param is required']}}, status=status.HTTP_400_BAD_REQUEST)


from apps.userProfile.models import UserProfile

class InterestGroupViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    queryset = InterestGroup.objects.exclude(slug='public')
    serializer_class = InterestGroupSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @detail_route(methods=['get'], permission_classes=[IsOwner])
    def members(self, request, pk=None):
        return super(InterestGroupViewSet, self).retrieve(request, pk=pk)

    @detail_route(methods=['post'], permission_classes=[IsOwner])
    def invite(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({'fields_errors': [{'email': ['This field is required']}]},
                            status=status.HTTP_400_BAD_REQUEST)

        suscription = Suscription()

        suscription.create(email=email, group=self.get_object())
        return Response({'message': ['success, invite member to this group']},
                            status=status.HTTP_202_ACCEPTED)

    @detail_route(methods=['delete'], permission_classes=[IsOwner])
    def remove_member(self, request, *args, **kwargs):
        profile_pk = request.query_params.get('user')
        #import ipdb; ipdb.set_trace()
        if not profile_pk:
            return Response({'fields_errors': [{'user': ['This field is required']}]},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            profile = UserProfile.objects.get(pk=profile_pk)
            profile.interest_groups.remove(self.get_object())
            #import pdb; pdb.set_trace()
            #for i in range(len(profile.interest_groups.all())-1):
            #    if profile.interest_groups[i].pk == group.pk:
            #        profile.interest_groups.pop(i)
            #        break
            profile.save()

        except UserProfile.DoesNotExist:
            return Response({'fields_errors': [{'user': ['This fields not belong to a member']}]},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': ['success, remove member to this group']},
                            status=status.HTTP_202_ACCEPTED)



    def get_queryset(self):
        return self.queryset.filter(members=self.request.user.profile)


class PostViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(group__pk=self.kwargs.get('group_pk'))


class InterestGroupDetail(DetailView):
    template_name = "interest_group/details.html"
    model = InterestGroup
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super(InterestGroupDetail, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['subscription'] = Suscription.objects.filter(group=self.object, user=self.request.user)
        else:
            context['subscription'] = None

        return context



class InvitationGroup(UpdateView):
    template_name = 'interest_group/invitation.html'
    model = Suscription
    form_class = SuscriptionForm
    queryset = Suscription.objects.filter(status=0)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(InvitationGroup, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            return self.queryset.get(email=self.request.user.email,
                                     hash_invitation=self.kwargs.get('hash'),
                                     group=self.kwargs.get('group_id'))
        except Suscription.DoesNotExist:
            return None

    def form_valid(self, form):
        suscription = form.clean()
        if suscription.get('status') == '1':
            profile = self.request.user.profile
            profile.interest_groups.add(self.object.group)
            profile.save()
            messages.success(self.request, "En hora buena! Disfrute de su nuevo grupo.")
        else:
            self.success_url = '/'
            messages.info(self.request, "Disculpe las molestias, ha rechazado el grupo correctamente.")

        response = super(InvitationGroup, self).form_valid(form)
        return response

    def get_success_url(self):
        # The superclass version raises ImproperlyConfigered if self.success_url
        # isn't set. Instead of that, we'll try to redirect to a named view.
        if self.success_url:
            return self.success_url
        else:
            #import pdb; pdb.set_trace()
            return reverse('group:detail', kwargs={ 'slug':self.object.group.slug})

    def get_context_data(self, **kwargs):
        context = super(InvitationGroup, self).get_context_data(**kwargs)
        context['suscription'] = self.get_object()
        return context