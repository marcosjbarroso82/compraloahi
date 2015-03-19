from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.comments.views.comments import post_comment
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'index.html'


class ApiDashBoardView(TemplateView):
    template_name = 'api/dashboard.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(ApiDashBoardView, self).dispatch(*args, **kwargs)


class DashBoardView(TemplateView):
    template_name = 'dashboard-ajax.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(DashBoardView, self).dispatch(*args, **kwargs)

class DashBoardAjaxView(TemplateView):
    template_name = 'userProfile/dashboard-ajax.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(DashBoardAjaxView, self).dispatch(*args, **kwargs)



def comment_post_wrapper(request):
    # Clean the request to prevent form spoofing
    if request.user.is_authenticated():
        # if not (request.user.get_full_name() == request.POST['name'] or \
        #        request.user.email == request.POST['email']):
        #     return HttpResponse("You registered user...trying to spoof a form...eh?")
        return post_comment(request) # VER SI ESTE ES EL POST, o EL DE COMMENT XTD
    return HttpResponse("You anonymous cheater...trying to spoof a form?")

# Generates Auth Tokens for all Users
class GenerateAllAuthToken(APIView):
    def get(self, request):
        response = "{"
        for user in User.objects.all():
            token, created = Token.objects.get_or_create(user=user)
            response += "{" + "username:" + user.username + ",pk: " + str(user.pk) + ",token:" + token.key + "},"
        response += "}"
        return Response(response)

generate_all_auth_token = GenerateAllAuthToken.as_view()