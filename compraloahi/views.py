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

from rest_framework import pagination

from django.utils.html import escape
from push_notifications.models import GCMDevice
from django.views.decorators.csrf import csrf_exempt

from apps.ad.models import Ad

from django.shortcuts import redirect

import logging

logger = logging.getLogger('debug')

@csrf_exempt
def log(request):
    #html = request
    logger.debug( request.body )
    #logger.debug( request.HEADERS )
    return HttpResponse( "algo" )
    #return HttpResponse( escape(repr(request)) )


# Test send notification to android
def send_notification(request):
    device = GCMDevice.objects.first()

    device.send_message(request.GET.get('msg', "Hola"))

    return HttpResponse("Notificacion enviada con exito")


class HomeView(TemplateView):
    template_name = 'dashboard/base.html'

    def dispatch(self, request, *args, **kwargs):
        return redirect('/ad/search/?q=')


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
        # In case of a reply, check that the user is answering a comment of his own ad
        object_pk = request.POST.get('object_pk', '')
        if int( request.POST.get('reply_to') ) > 0:
            if ( Ad.objects.get(pk=object_pk).author == request.user):
                return post_comment(request) # VER SI ESTE ES EL POST, o EL DE COMMENT XTD
        else:
            if ( Ad.objects.get(pk=object_pk).author != request.user):
                return post_comment(request) # VER SI ESTE ES EL POST, o EL DE COMMENT XTD

    return HttpResponse('Unauthorized', status=401)

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



class CustomPagination(pagination.PageNumberPagination):
    """
        Custom pagination
            return only page number in next and previous pages.
    """
    def get_paginated_response(self, data):
        resp = {}
        if self.page.has_next():
            resp['next']  = self.page.next_page_number()
        else:
            resp['next']  = None

        if self.page.has_previous():
            resp['previous'] = self.page.previous_page_number()
        else:
            resp['previous'] = None

        resp['count'] = self.page.paginator.count
        resp['results'] = data
        return Response(resp)