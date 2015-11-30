from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.favorite.views import HasFavoriteNearApiView

from apps.userProfile.views import StoreView
from apps.user.views import FacebookLogin, GoogleLogin

from .views import HomeView, DashBoardView, log, send_notification, TermAndConditionView
from django.views.generic import TemplateView
from .settings import base as settings
from apps.util.views import RegisterInterested, TemplateMessage, ContactFormView

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view()),

                       url(r'^report-error/$', 'apps.report_error.views.report_error', name='report-error'),

                       url('^interested/$', RegisterInterested.as_view(), name='interested-app'),
                       url('^dynamic-message/$', TemplateMessage.as_view(), name='dynamic-message'),
                       url(r'^face/$', 'apps.util.views.register_count_whered', {'whered': 'facebook'}),
                       url(r'^contactenos/$', ContactFormView.as_view(), name='contact'),

                       # TODO : This url belong to api
                       url(r'^favorites/near/$', HasFavoriteNearApiView.as_view() , name='favorite-near'),

                       url(r'^oportunidades-anunciante/$', TemplateView.as_view(template_name='oportunidades-anunciante.html')),

                       url(r'^oportunidades-interesado/$', TemplateView.as_view(template_name='oportunidades-interesado.html')),

                       # TODO: Esta url no va en produccion
                       url(r'^log/', log),

                       url('^faq/', include('apps.faq.urls')),

                       url('^terminosycondiciones/(?P<template>.*)$', TermAndConditionView.as_view()),

                       # Terms and Conditions
                       #url(r'^terms/', include('termsandconditions.urls')),

                        # Include API
                       (r'^api/v1/', include('compraloahi.urls_api', namespace='api')),

                       # TODO : This url belong to api
                       url(r'^rest-auth/facebook/$',
                           FacebookLogin.as_view(),
                           name='fb_login'),

                        # TODO : This url belong to api
                       url(r'^rest-auth/google/$',
                           GoogleLogin.as_view(),
                           name='goo_login'),

                        # Add authentication by django rest client
                        #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                        # TODO : This url belong to api
                       url(r'^rest-auth/', include('rest_auth.urls')),
                       url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

                       # TODO: Esta url no va en produccion
                       url(r'^send_notification/', send_notification),

                       url(r'^favorite/' , include('apps.favorite.urls', namespace='favorite')),

                       # URL load dashboard
                       url(r'^panel/.*$', DashBoardView.as_view(), name='dashboard'),

                       # Admin django
                       url(r'^admin/', include(admin.site.urls)),

                       # My apps Ad
                       url(r'^item/', include("apps.ad.urls", namespace="ad")),

                       # My apps User
                       (r'^users/',
                        include('apps.user.urls',
                                namespace='my-user')),

                        url(r'^calification/', include('apps.rating.urls', namespace="rating")),

                       # App Allauth (social authentication)
                       (r'^accounts/', include('allauth.urls')),


                       # Parche comments
                       (r'^comments/post/$',
                        'compraloahi.views.comment_post_wrapper'),

                       # Package comments
                       (r'^comments/', include('django_comments_xtd.urls')),

                       # Files Media
                       url(r'^media/(?P<path>.*)$',
                           "django.views.static.serve",
                           {'document_root': settings.MEDIA_ROOT}),

                       url(r'^tienda/(?P<slug>[a-zA-Z0-9_.-]+)/$',
                           StoreView.as_view(),
                           name="store"),

                       )
