from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView

from .models import UserProfile, UserLocation, Phone
from .forms import UserProfileForm, Phone_inline_formset, Location_inline_formset

from rest_framework.viewsets import ModelViewSet

from .serializers import UserProfileSerializer, UserLocationSeralizer
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
import ast

class UserProfileModelView(ModelViewSet):
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(self.get_queryset())
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            profile = self.get_queryset()
            profile.birth_date = request.DATA['birth_date']

            if request.FILES.get('image', None):
                profile.image = request.FILES['image']

            print(request.DATA)
            user_data = ast.literal_eval(request.DATA['user'])

            user = profile.user
            print("FIRST NAME")
            print(user_data)
            user.first_name = user_data['first_name']
            user.last_name = user_data['last_name']
            user.email = user_data['email']

            #Delete all phones to user
            Phone.objects.filter(userProfile=profile).delete()

            phones_data = ast.literal_eval(request.DATA['phones'])
            #Add new phone
            for phone in phones_data:
                p = Phone()
                p.userProfile = profile
                p.number= int(phone['number'])
                p.type = phone['type']
                p.save()

            profile.save()
            user.save()

            return Response({'status': 'Ok request.', 'message': 'Los datos de usuario se modificaron con exito'}, status=status.HTTP_200_OK )
        except KeyError:
            return Response({'status': 'Bad request.', 'message': "ERROR: You need Complete all fields"}, status=status.HTTP_400_BAD_REQUEST)

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
        locations_form = Location_inline_formset()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                phones_form=phones_form,
                locations_form=locations_form))

    def post(self, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        # Phones
        phones_form = Phone_inline_formset(
            self.request.POST, self.request.FILES, instance=form.instance)

        locations_form = Location_inline_formset( self.request.POST, self.request.FILES, instance=form.instance)

        if form.is_valid() and phones_form.is_valid() and locations_form.is_valid():
            return self.form_valid(form, phones_form, locations_form)
        else:
            return self.form_invalid(form, phones_form, locations_form)

    def form_valid(self, form, phones_form, locations_form):
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

        # look, validate and save all locations
        for location_form in locations_form:
            location_form.instance.userProfile = form.instance
            location_form.instance.title = location_form.cleaned_data.get('title')
            location_form.instance.lat = location_form.cleaned_data.get('lat')
            location_form.instance.lng = location_form.cleaned_data.get('lng')
            if location_form.is_valid():
                location_form.save()

        return super(UserProfileCreateView, self).form_valid(form)

    def form_invalid(self, form, phones_form, locations_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                phones_form=phones_form,
                locations_form=locations_form))



class UserProfileUpdateView(UpdateView):
    model = UserProfile
    success_url = '/accounts/profile'
    form_class = UserProfileForm
    template_name = 'userProfile/update.html'

    def get_object(self, queryset=None):
        return UserProfile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.form_class)

        if self.request.method == 'POST':
            context['phones_form'] = Phone_inline_formset(
                self.request.POST, self.request.FILES, instance=self.object)
            context['locations_form'] = Location_inline_formset(
                self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['phones_form'] = Phone_inline_formset(instance=self.object)
            context['locations_form'] = Location_inline_formset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        phones_formset = context['phones_form']
        locations_formset = context['locations_form']
        form.save(commit=False)

        user = self.request.user
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.save()

        # Phones
        for phone_form in phones_formset:
            if phone_form.is_valid():
                phone_form.instance.type = phone_form.cleaned_data.get('type')
                phone_form.instance.number = phone_form.cleaned_data.get('number')
                if phone_form.is_valid():
                    phone_form.save()

        for phone_form in phones_formset.deleted_forms:
            phone_form.instance.delete()

        # Locations
        for location_form in locations_formset:
            if location_form.is_valid():
                location_form.instance.title = location_form.cleaned_data.get('title')
                location_form.instance.lat = location_form.cleaned_data.get('lat')
                location_form.instance.lng = location_form.cleaned_data.get('lng')
                location_form.save()

        for location_form in locations_formset.deleted_forms:
            location_form.instance.delete()

        return super(UserProfileUpdateView, self).form_valid(form)


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'userProfile/dashboard.html'
    context_object_name = 'profile'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.get_object():
            return super(UserProfileDetailView, self).dispatch(*args, **kwargs)
        else:
            return HttpResponseRedirect('/accounts/profile/create/')

    def get_object(self, queryset=None):
        try:
            return UserProfile.objects.get(user=self.request.user)
        except:
            return None

class UserLocationViewSet(viewsets.ModelViewSet):

    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSeralizer
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('title', 'slug', 'id')

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.DATA)
        serializer.is_valid()
        serializer.save(userProfile=UserProfile.objects.get(user=request.user))
        return Response({'status': 'Ok request.', 'message': 'Los datos de usuario se modificaron con exito'}, status=status.HTTP_201_CREATED )




