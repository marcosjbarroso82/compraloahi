from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from django.views.generic import View

from .serializers import UserSerializer
from rest_framework.generics import RetrieveAPIView


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