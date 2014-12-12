from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from django.views.generic import View

from .serializers import UserSerializer
from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response


class UserRetrieveView(RetrieveAPIView):

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return self.request.user



class LogoutView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

        print("PASSWORD :" + request.DATA['password'])
        print("PASSWORD NEW :" + request.DATA['new_password'])
        print("PASSWORD NEW REPEAT :" + request.DATA['new_password_repeat'])
        user = request.user
        if user.check_password(request.DATA['password']):
            if request.DATA['new_password'] == request.DATA['new_password_repeat']:
                user.set_password(request.DATA['new_password'])
                user.save()
                return Response({'status': 'Ok request.', 'message': 'La contraseña se modifico con exito'}, status=status.HTTP_200_OK )
            else:
                return Response({'status': 'Bad request.', 'message': 'Las contraseñas no cohinciden'}, status=status.HTTP_400_BAD_REQUEST )
        else:
            return Response({'status': 'Bad request.', 'message': 'La contraseña actual es incorrecta'}, status=status.HTTP_400_BAD_REQUEST )