from django.views.generic import DetailView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_framework.generics import UpdateAPIView

from sorl.thumbnail import get_thumbnail

from apps.ad.models import Ad

from .models import UserProfile, UserLocation, Store
from .serializers import ProfileSerializer, UserLocationSeralizer, StoreSerializer, ProfileLocationSerializer, ConfigPrivacitySerializer


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
    template_name = 'userProfile/shop.html'
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



class UserLocationViewSet(ModelViewSet):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSeralizer

    def get_queryset(self):
        return UserLocation.objects.filter(userProfile__user= self.request.user, is_address=False)



# class ProfileLocationUpdateAPI(UpdateAPIView):
#     serializer_class = ProfileLocationSerializer
#     queryset = UserLocation.objects.filter(is_address=True)
#
#     def get_object(self):
#         print(30*"====")
#         print("GET OBJECT")
#         try:
#             return UserLocation.objects.get(is_address=True)
#         except UserLocation.DoesNotExist:
#             return {}
#         #except:
#             # Save exception to revision
#         #    return UserLocation.objects.filter(is_address=True).first()


class ProfileLocationViewSet(ModelViewSet):
    """
        ModelViewSet to abm for address to profile user
    """
    queryset = UserLocation.objects.filter(is_address=True)
    serializer_class = ProfileLocationSerializer

    def get_queryset(self):
        return self.queryset.filter(userProfile__user= self.request.user)

    def get_object(self):
        try:
            return UserLocation.objects.get(is_address=True, userProfile__user= self.request.user)
        except UserLocation.DoesNotExist:
            return {}



class ConfigPrivacityViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ConfigPrivacitySerializer

    def get_object(self):
        return self.request.user.profile

