from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from django.views.generic import View

from .serializers import UserSerializer
from rest_framework.generics import UpdateAPIView

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response



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
                return Response({'status': 'Ok request.', 'message': 'La contraseña se modifico con exito'}, status=status.HTTP_200_OK )
            else:
                return Response({'status': 'Bad request.', 'message': 'Las contraseñas no cohinciden'}, status=status.HTTP_400_BAD_REQUEST )
        else:
            return Response({'status': 'Bad request.', 'message': 'La contraseña actual es incorrecta'}, status=status.HTTP_400_BAD_REQUEST )