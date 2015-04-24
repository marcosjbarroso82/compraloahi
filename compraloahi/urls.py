from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from apps.ad import views as adViews
from apps.favorite.views import FavoriteAdViewSet, HasFavoriteNearApiView
from apps.message.views import MessageDetail, MessageModelViewSet
from apps.notification.views import NotificationListApiView, NotificationRetrieveApiView, \
    RegisterGCMNotification, UnregisterGCMNotification, NotificationMarkBulkReadApiView
from apps.userProfile.views import UserLocationViewSet, UserProfileModelView
from apps.user.views import ChangePasswordUpdateAPIView, FacebookLogin, GoogleLogin

from .views import HomeView, ApiDashBoardView, DashBoardAjaxView, log, send_notification, generate_all_auth_token
from . import settings_old


router = DefaultRouter()
router.register(r'my-ads', adViews.AdUserViewSet)
router.register(r'ads', adViews.AdPublicViewSet)
router.register(r'user-locations', UserLocationViewSet)
router.register(r'favorites', FavoriteAdViewSet)

router.register(r'ad-search', adViews.SearchViewSet, base_name='search') #/api/v1/ad-search/?q=algo&latitude=-31&longitude=-64&km=33

urlpatterns = patterns('',
                       url(r'^favorites/near/$', HasFavoriteNearApiView.as_view() , name='favorite-near'),
                       url(r'^log/', log),
                       url(r'^api/v1/notifications/bulk/$',NotificationMarkBulkReadApiView.as_view(), name='notification-marked-bulk-read'),
                       url(r'^api/v1/notifications/(?P<pk>\d+)/$',NotificationRetrieveApiView.as_view(), name='notification-marked-read'),
                       url(r'^api/v1/notifications/$', NotificationListApiView.as_view(), name='notifications-user'),

                       url(r'^api/v1/notification/register/$', RegisterGCMNotification.as_view(), name='not-register'),
                       url(r'^api/v1/notification/unregister/$', UnregisterGCMNotification.as_view(), name='not-unregister'),

                       url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
                       url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='goo_login'),
                       url(r'^rest-auth/', include('rest_auth.urls')),
                       url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

                       url(r'^send_notification/', send_notification),


                       url(r'^favit/' , include('favit.urls')),
                       url(r'^api-generate-all-token-auth/', generate_all_auth_token),
                       url(r'^api-token-auth/', views.obtain_auth_token),

                       url(r'^api/v1/', include(router.urls)),

                       # Detail Profile
                       url(r'^api/v1/profile/$',
                           UserProfileModelView.as_view({'get': 'retrieve'}),
                           name='api-profile-detail'),

                        # Create Profile by API
                       #url(r'^api/v1/profile/create/$',
                       #    UserProfileModelView.as_view({'post': 'create'}),
                       #    name='api-profile-detail'),

                       # Update Profile
                       url(r'^api/v1/profile/(?P<pk>\d+)/$',
                           UserProfileModelView.as_view({'put': 'update'}),
                           name='api-profile-update'),



                       # Change password
                       url(r'^api/v1/change-password/$',
                           ChangePasswordUpdateAPIView.as_view(),
                           name='api-change-password'),

                       # Login and logout (DjangoRestFramework)
                       url(r'^api/v1/',
                           include('rest_framework.urls',
                                   namespace='rest_framework')),

                       url(r'^dashboard-ajax/.*$',
                           DashBoardAjaxView.as_view(),
                           name='dashboard-ajax'),
                       url(r'^$', HomeView.as_view()),

                       # API Message List
                       url(r'^api/v1/messages/thread/(?P<pk>\d+)/$',
                           MessageModelViewSet.as_view({'get': 'retrieve'})),

                       url(r'^api/v1/messages/(?P<pk>\d+)/$',
                           MessageDetail.as_view()),

                       url(r'^api/v1/messages/(?P<folder>\w+)/$',
                           MessageModelViewSet.as_view({'get': 'list'}),
                           name='api-message-list'),

                       url(r'^api/v1/messages/$',
                           MessageModelViewSet.as_view({'get': 'list_all', 'post': 'create'}),
                           name='api-message-list-all'),

                       url(r'^api/v1/messages/delete-bulk/$',
                           'apps.message.views.message_bulk_delete',
                           name='api-message-delete-bulk'),


                       url(r'^api/v1/messages/set-read-bulk/$',
                           'apps.message.views.message_bulk_set_read',
                           name='api-message-set-read-bulk'),

                       url(r'^dashboard/.*$',
                           ApiDashBoardView.as_view(),
                           name='dashboard'),
                       # Admin django
                       url(r'^admin/', include(admin.site.urls)),

                       # My apps Ad
                       url(r'^ad/', include("apps.ad.urls", namespace="ad")),

                       # My apps User
                       (r'^users/',
                        include('apps.user.urls',
                                namespace='my-user')),

                       # App Allauth (social authentication)
                       (r'^accounts/', include('allauth.urls')),

                       # My app Profile
                       (r'^accounts/',
                        include('apps.userProfile.urls',
                                namespace="profile")),

                       # Package Postman Messages
                       (r'^messages/', include('postman.urls')),

                       # Override package postman
                       (r'^message/',
                        include('apps.message.urls',
                                namespace="message")),

                       # Packages ckeditor
                       (r'^ckeditor/', include('ckeditor.urls')),

                       # Parche comments
                       (r'^comments/post/$',
                        'compraloahi.views.comment_post_wrapper'),

                       # Package comments
                       (r'^comments/', include('django_comments_xtd.urls')),

                       # Files Media
                       url(r'^media/(?P<path>.*)$',
                           "django.views.static.serve",
                           {'document_root': settings_old.MEDIA_ROOT}),

                       )
