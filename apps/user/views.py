from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from django.views.generic import View

from .serializers import UserSerializer, DeviceSerializer
from rest_framework.generics import UpdateAPIView, CreateAPIView

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLogin

from rest_framework.decorators import api_view
from push_notifications.models import GCMDevice

class RegisterNotificatin(CreateAPIView):
    serializer_class = DeviceSerializer


class UnregisterNotification(UpdateAPIView):
    serializer_class = DeviceSerializer
    # TODO: Pasar funcionalidad al serializer
    def update(self, request, *args, **kwargs):
        if request.DATA.get('registration_id', '') != '':
            try:
                gcm = GCMDevice.objects.get(user=request.user, registration_id= request.DATA.get('registration_id'))
                gcm.active = False
                gcm.save()
                return Response({"message": "Success! User unregistered to notification"}, status=status.HTTP_200_OK)
            except GCMDevice.DoesNotExist:
                return Response({'message': "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': "Field registration id is required."}, status=status.HTTP_400_BAD_REQUEST)


class FacebookLogin(SocialLogin):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLogin):
    adapter_class = GoogleOAuth2Adapter


class LogoutView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')



class ChangePasswordUpdateAPIView(UpdateAPIView):
    """
        Funcion api para cambiar contraseña del usuario autenticado
        Parametros
            password: password actual
            new-password: nuevo password
            new-password-repeat: repite nuevo password
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def partial_update(self, request, *args, **kwargs):

        user = request.user
        if user.check_password(request.DATA.get('password', None)):
            if request.DATA['new_password'] == request.DATA['new_password_repeat']:
                user.set_password(request.DATA['new_password'])
                user.save()
                return Response({'message': 'La contraseña se modifico con exito'}, status=status.HTTP_200_OK )
            else:
                return Response({'message': 'Las contraseñas no cohinciden'}, status=status.HTTP_400_BAD_REQUEST )
        else:
            return Response({'message': 'La contraseña actual es incorrecta'}, status=status.HTTP_400_BAD_REQUEST )