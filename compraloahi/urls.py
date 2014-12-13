from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomeView, ApiDashBoardView, DashBoardAjaxView
from . import settings

from apps.ad import views as adViews
from apps.user import views as userViews
from apps.userProfile.views import UserProfileModelView
from apps.message.views import MessageList, MessageDetail, MessageModelViewSet

from rest_framework.routers import DefaultRouter

from apps.user.views import ChangePasswordUpdateAPIView

router = DefaultRouter()
router.register(r'ads', adViews.AdViewSet)
#router.register(r'users', userViews.UserViewSet)
urlpatterns = patterns('',
                        url(r'^api/v1/', include(router.urls)),

                        # Detail Profile
                        url(r'^api/v1/profile/$', UserProfileModelView.as_view({'get': 'retrieve'}), name='api-profile-detail' ),
                        # Update Profile
                        url(r'^api/v1/profile/$', UserProfileModelView.as_view({'put': 'update'}), name='api-profile-detail' ),

                        # Change password
                        url(r'^api/v1/change-password/$', ChangePasswordUpdateAPIView.as_view(), name='api-change-password' ),

                        # Login and logout (DjangoRestFramework)
                        url(r'^api/v1/', include('rest_framework.urls', namespace='rest_framework')),

                        url(r'^dashboard-ajax/.*$', DashBoardAjaxView.as_view(), name='dashboard-ajax'),
                        url(r'^$', HomeView.as_view()),

                        # API Message List
                        url(r'^api/v1/messages/thread/(?P<pk>\d+)/$', MessageModelViewSet.as_view({'get': 'retrieve'})),

                        url(r'^api/v1/messages/(?P<pk>\d+)/$', MessageDetail.as_view()),

                        url(r'^api/v1/messages/(?P<folder>\w+)/$', MessageModelViewSet.as_view({'get': 'list'}), name='api-message-list'),


                        url(r'^dashboard/.*$', ApiDashBoardView.as_view(), name='dashboard' ),
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


                        )




