from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_auth.registration.views import SocialLoginView

from .serializers import UserSerializer


class FacebookOAuth2AdapterCustom(FacebookOAuth2Adapter):
    """
	Patch to fix django-rest-auth
    """
    def __init__(self):
        pass

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2AdapterCustom


class GoogleOAuth2AdapterCustom(GoogleOAuth2Adapter):
    """
	Patch to fix django-rest-auth
    """
    def __init__(self):
        pass

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2AdapterCustom


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
        if user.check_password(request.data.get('password', None)):
            if request.data['new_password'] == request.data['new_password_repeat']:
                user.set_password(request.data['new_password'])
                user.save()
                return Response({'message': 'La contraseña se modifico con exito'}, status=status.HTTP_200_OK )
            else:
                return Response({'message': 'Las contraseñas no cohinciden'}, status=status.HTTP_400_BAD_REQUEST )
        else:
            return Response({'message': 'La contraseña actual es incorrecta'}, status=status.HTTP_400_BAD_REQUEST )


@api_view(['GET',])
def username_is_unique(request, *args, **kwargs):
    if request.user and kwargs.get('username'):
        if User.objects.filter(username=kwargs.get('username')).exclude(pk=request.user.id).count() > 0:
            return Response({'is_valid': "false", 'message': "This username exist."})

    return Response({'is_valid': "true", 'message': "This username is valid"})
