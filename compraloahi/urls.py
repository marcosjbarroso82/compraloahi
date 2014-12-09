from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomeView, ApiDashBoardView
from . import settings

from rest_framework import routers

from apps.ad.api import AdResource
from tastypie.api import Api

# Import views to api
from apps.userProfile.views import UserProfileModelView
from apps.user.views import UserRetrieveView

dashboard_api = Api(api_name='dashboard')
dashboard_api.register(AdResource())

router = routers.SimpleRouter()



urlpatterns = patterns('',
                        url(r'^$', HomeView.as_view()),

                        #### URL API
                        url(r'^api/v1/', include(router.urls, namespace="api", app_name="api-dashboard")),

                        # Probando
                        url(r'^api/v1/profile/$', UserProfileModelView.as_view({'get': 'retrieve'}), name='api-profile-detail' ),
                        url(r'^api/v1/user/$', UserRetrieveView.as_view(), name='api-user-detail' ),

                        url(r'^api/v1/.*$', ApiDashBoardView.as_view(), name='dashboard' ),
                        #### END URL API

                        # Admin django
                        url(r'^admin/', include(admin.site.urls)),

                        # My apps Ad
                        url(r'^ad/', include("apps.ad.urls", namespace="ad")),

                        #My apps User
                        (r'^users/', include('apps.user.urls', namespace='my-user')),

                        # App Allauth (social authentication)
                        (r'^accounts/', include('allauth.urls')),

                        # My app Profile
                        (r'^accounts/', include('apps.userProfile.urls', namespace="profile")),

                        # Package Postman Messages
                        (r'^messages/', include('postman.urls')),

                        # Override package postman
                        (r'^message/', include('apps.message.urls', namespace="message")),

                        # Packages ckeditor
                        (r'^ckeditor/', include('ckeditor.urls')),

                        # Package comments
                        (r'^comments/', include('django_comments_xtd.urls')),

                        # Files Media
                        url(r'^media/(?P<path>.*)$',
                           "django.views.static.serve",
                           {'document_root': settings.MEDIA_ROOT}),

                        (r'^api/', include(dashboard_api.urls)),

                        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                        )
