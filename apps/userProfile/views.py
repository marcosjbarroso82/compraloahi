from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from .models import UserProfile, UserLocation, Phone
from .forms import UserProfileForm, Phone_inline_formset

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

    # Code to found create profile by API
    # def create(self, request, *args, **kwargs):
    #     try:
    #         profile = UserProfile()
    #         profile.birth_date = request.DATA['birth_date']
    #
    #         if request.FILES.get('image', None):
    #             profile.image = request.FILES['image']
    #
    #         user_data = ast.literal_eval(request.DATA['user'])
    #
    #         user = request.user
    #         user.first_name = user_data['first_name']
    #         user.last_name = user_data['last_name']
    #         user.email = user_data['email']
    #
    #         profile.user = user
    #
    #         profile.save()
    #         user.save()
    #
    #         phones_data = ast.literal_eval(request.DATA['phones'])
    #         #Add new phone
    #         for phone in phones_data:
    #             p = Phone()
    #             p.userProfile = profile
    #             p.number= int(phone['number'])
    #             p.type = phone['type']
    #             p.save()
    #
    #         return Response({'status': 'Ok request.', 'message': 'Success! create profile'}, status=status.HTTP_200_OK )
    #     except KeyError:
    #         return Response({'status': 'Bad request.', 'message': "Error"}, status=status.HTTP_400_BAD_REQUEST)

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


class UserLocationViewSet(viewsets.ModelViewSet):
    # TODO : Falta filtrar ubicaciones por usuario
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSeralizer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.DATA)
        serializer.is_valid()
        obj = serializer.save(userProfile=UserProfile.objects.get(user=request.user))
        # TODO: For this to be a TRUE Rest Full Service API, It should return the same object that has just created
        #return Response({'status': 'Ok request.', 'message': 'Los datos de usuario se modificaron con exito'}, status=status.HTTP_201_CREATED )
        return Response({'id': obj.id,
                         'lat': obj.lat,
                         'lng': obj.lng,
                         'radius': obj.radius,
                         'title': obj.title,
                         'status': 'Ok request.', 'message': 'Los datos de usuario se modificaron con exito'}, status=status.HTTP_201_CREATED )

    def get_queryset(self):
        return UserLocation.objects.filter(userProfile__user= self.request.user)




