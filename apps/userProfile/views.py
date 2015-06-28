from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from .models import UserProfile, UserLocation, Store
from .forms import UserProfileForm, Phone_inline_formset

from rest_framework.viewsets import ModelViewSet

from .serializers import ProfileSerializer, UserLocationSeralizer, StoreSerializer
from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import api_view

from sorl.thumbnail import get_thumbnail

from apps.ad.models import Ad



class StoreModelViewSet(ModelViewSet):
    serializer_class = StoreSerializer

    def get_object(self):
        return Store.objects.get(profile__user= self.request.user)

    def get_queryset(self):
        return Store.objects.get(profile__user= self.request.user)


    def update(self, request, *args, **kwargs):
        if request.DATA.get('ads'):
            for ad_data in request.DATA.get('ads'):
                try:
                    print(ad_data['store_published'])
                    ad = Ad.objects.get(pk=ad_data['id'], author=request.user)
                    ad.store_published = ad_data.get('store_published', False)
                    ad.save()
                except Ad.DoesNotExist:
                    pass
                except:
                    pass

            return super(StoreModelViewSet, self).update(request, *args, **kwargs)
        else:
            return super(StoreModelViewSet, self).update(request, *args, **kwargs)
            #return Response({'ads': ['Need a or more ads to config config store']})


class StoreView(DetailView):
    model = Ad
    template_name = 'userProfile/store.html'
    context_object_name = 'store'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(StoreView, self).get_context_data(**kwargs)
        context['param_url'] = self.kwargs.get('slug', '')
        context['ads'] = Ad.objects.filter(author=self.object.profile.user, store_published=True)
        return context

    def get_object(self, queryset=None):
        try:
            return Store.objects.get(slug=self.kwargs.get('slug', ''), status=1)
        except Store.DoesNotExist:

            # TODO: Return page doesnt exist
            return {}


@api_view(['GET',])
def store_name_is_unique(request, *args, **kwargs):
    if request.user and kwargs.get('slug'):
        if Store.objects.filter(name=kwargs.get('slug')).exclude(profile__user=request.user.id).count() > 0:
            return Response({'is_valid': "false", 'message': "This store name exist."})

    return Response({'is_valid': "true", 'message': "This store name is valid"})


@api_view(['GET', 'POST', ])
def upload_logo_store(request):
    if request.method == 'POST':
        if request.FILES.get('image'):
            request.user.profile.store.logo = request.FILES.get('image')
            request.user.profile.store.save()

            return Response({
                                'status': 'Ok request',
                                'message': 'Set data ok.',
                                'image_url': request.user.profile.store.logo.url
                            }, status=status.HTTP_200_OK)



@api_view(['GET', 'POST', ])
def upload_image_profile(request):
    if request.method == 'POST':
        if request.FILES.get('image'):
            request.user.profile.image = request.FILES.get('image')
            request.user.profile.save()


            return Response({
                                'status': 'Ok request',
                                'message': 'Set data ok.',
                                'image_url': get_thumbnail(request.user.profile.image, '400x400', crop='center', quality=99).url
                            }, status=status.HTTP_200_OK)


class UserProfileModelView(ModelViewSet):
    serializer_class = ProfileSerializer

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

    def get_queryset(self):
        return UserProfile.objects.get(user=self.request.user)


class UserProfileCreateView(CreateView):
    model = UserProfile
    success_url = '/accounts/profile/'
    form_class = UserProfileForm
    template_name = 'userProfile/create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfileCreateView, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phones_form = Phone_inline_formset()
        #locations_form = Location_inline_formset()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                phones_form=phones_form))
                #locations_form=locations_form))

    def post(self, *args, **kwargs):
        # If has next, the success url change
        if self.request.GET.get('next', None):
            self.success_url =  self.request.GET['next']

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        # Phones
        phones_form = Phone_inline_formset(
            self.request.POST, self.request.FILES, instance=form.instance)

        if form.is_valid() and phones_form.is_valid():
            return self.form_valid(form, phones_form)
        else:
            return self.form_invalid(form, phones_form)

    def form_valid(self, form, phones_form): #, locations_form):
        user = self.request.user
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.save()

        form.save(commit=False)
        form.instance.user = user
        form.instance.save()
        # look, validate and save all phones
        for phone_form in phones_form:
            phone_form.instance.userProfile = form.instance
            phone_form.instance.type = phone_form.cleaned_data.get('type')
            phone_form.instance.number = phone_form.cleaned_data.get('number')
            if phone_form.is_valid():
                phone_form.save()

        return super(UserProfileCreateView, self).form_valid(form)

    def form_invalid(self, form, phones_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                phones_form=phones_form))


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'userProfile/dashboard.html'
    context_object_name = 'profile'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfileDetailView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        try:
            return UserProfile.objects.get(user=self.request.user)
        except:
            return None


class UserLocationViewSet(ModelViewSet):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSeralizer
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.DATA)
    #     serializer.is_valid()
    #     obj = serializer.save(userProfile=request.user.profile)
    #     # TODO: For this to be a TRUE Rest Full Service API, It should return the same object that has just created
    #     #return Response({'status': 'Ok request.', 'message': 'Los datos de usuario se modificaron con exito'}, status=status.HTTP_201_CREATED )
    #     return Response({'id': obj.id,
    #                      'lat': obj.lat,
    #                      'lng': obj.lng,
    #                      'radius': obj.radius,
    #                      'title': obj.title,
    #                      'status': 'Ok request.', 'message': 'Los datos de usuario se modificaron con exito'}, status=status.HTTP_201_CREATED )

    def get_queryset(self):
        return UserLocation.objects.filter(userProfile__user= self.request.user)





