from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.favorite.views import HasFavoriteNearApiView

from apps.userProfile.views import StoreView
from apps.user.views import FacebookLogin, GoogleLogin

from .views import HomeView, DashBoardView, log, send_notification

from .settings import base as settings


urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view()),

                       # TODO : This url belong to api
                       url(r'^favorites/near/$', HasFavoriteNearApiView.as_view() , name='favorite-near'),

                       # TODO: Esta url no va en produccion
                       url(r'^log/', log),

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

                        # TODO : This url belong to api
                       url(r'^rest-auth/', include('rest_auth.urls')),
                       url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

                       # TODO: Esta url no va en produccion
                       url(r'^send_notification/', send_notification),

                       url(r'^favit/' , include('favit.urls')),

                       # URL load dashboard
                       url(r'^panel/.*$', DashBoardView.as_view(), name='dashboard'),

                       # Admin django
                       url(r'^admin/', include(admin.site.urls)),

                       # My apps Ad
                       url(r'^ad/', include("apps.ad.urls", namespace="ad")),

                       # My apps User
                       (r'^users/',
                        include('apps.user.urls',
                                namespace='my-user')),

                        url(r'^calification/', include('apps.rating.urls', namespace="rating")),

                       # App Allauth (social authentication)
                       (r'^accounts/', include('allauth.urls')),

                       # Package Postman Messages
                       (r'^messages/', include('postman.urls')),

                       # Override package postman
                       (r'^message/', include('apps.message.urls', namespace="message")),

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
