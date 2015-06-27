from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from apps.ad.views import AdUserViewSet, AdPublicViewSet, SearchViewSet, CategoriesListAPIView
from apps.favorite.views import FavoriteAdViewSet, proximityFavorityApiView
from apps.message.views import MessageDetail, MessageModelViewSet
from apps.notification.views import NotificationListApiView, NotificationRetrieveApiView, \
    RegisterGCMNotification, UnregisterGCMNotification, NotificationMarkBulkReadApiView, ConfigNotificationModelViewSet
from apps.user.views import ChangePasswordUpdateAPIView
from apps.userProfile.views import UserLocationViewSet, UserProfileModelView, StoreModelViewSet

from .views import generate_all_auth_token


router = DefaultRouter()
router.register(r'my-ads', AdUserViewSet, base_name='ad-by-user')
router.register(r'ads', AdPublicViewSet, base_name='ads')
router.register(r'user-locations', UserLocationViewSet, base_name='location-by-user')
router.register(r'favorites', FavoriteAdViewSet, base_name='favorites')
router.register(r'ad-search', SearchViewSet, base_name='search') #/ad-search/?q=algo&latitude=-31&longitude=-64&km=33


urlpatterns = patterns('',
                       url(r'^categories/$', CategoriesListAPIView.as_view(), name='categories'),

                       url(r'^favorites/(?P<lat>[a-zA-Z0-9_.-]+)/(?P<lng>[a-zA-Z0-9_.-]+)/$',
                           proximityFavorityApiView.as_view() ,
                           name='proximity-favorite'),

                       url(r'^store-config/$',
                           StoreModelViewSet.as_view({'get': 'retrieve', 'put': 'update'}),
                           name='store-config'),

                       url(r'^notifications-config/$',
                           ConfigNotificationModelViewSet.as_view({'get': 'retrieve', 'put': 'update'}),
                           name='notification-config'),

                       url(r'^notifications/bulk/$',
                           NotificationMarkBulkReadApiView.as_view(),
                           name='notification-marked-bulk-read'),

                       url(r'^notifications/(?P<pk>\d+)/$',
                           NotificationRetrieveApiView.as_view(),
                           name='notification-marked-read'),

                       url(r'^notifications/$',
                           NotificationListApiView.as_view(),
                           name='notifications-user'),

                       url(r'^notification/register/$',
                           RegisterGCMNotification.as_view(),
                           name='not-register'),
                       url(r'^notification/unregister/$',
                           UnregisterGCMNotification.as_view(),
                           name='not-unregister'),

                       # TODO : Esta url hay que desactivarla en produccion?
                       url(r'^api-generate-all-token-auth/', generate_all_auth_token),

                       url(r'^api-token-auth/', obtain_auth_token),

                       # Detail Profile
                       url(r'^profile/$',
                           UserProfileModelView.as_view({'get': 'retrieve', 'put': 'update'}),
                           name='api-profile-detail'),

                       url(r'^change-image/$',
                           'apps.userProfile.views.upload_image_profile', name='api-profile-change-image'),

                       # Change password
                       url(r'^change-password/$',
                           ChangePasswordUpdateAPIView.as_view(),
                           name='api-change-password'),

                       url('^username-is-unique/(?P<username>.+)/$',
                           'apps.user.views.username_is_unique',
                           name='api-user-username-is-unique'),

                       # Login and logout (DjangoRestFramework)
                       url(r'^',
                           include('rest_framework.urls',
                                   namespace='rest_framework')),

                       # API Message List
                       url(r'^messages/thread/(?P<pk>\d+)/$',
                           MessageModelViewSet.as_view({'get': 'retrieve'})),

                       url(r'^messages/(?P<pk>\d+)/$',
                           MessageDetail.as_view()),

                       url(r'^messages/(?P<folder>\w+)/$',
                           MessageModelViewSet.as_view({'get': 'list'}),
                           name='api-message-list'),

                       url(r'^messages/$',
                           MessageModelViewSet.as_view({'get': 'list_all', 'post': 'create'}),
                           name='api-message-list-all'),

                       url(r'^messages/delete-bulk/$',
                           'apps.message.views.message_bulk_delete',
                           name='api-message-delete-bulk'),


                       url(r'^messages/set-read-bulk/$',
                           'apps.message.views.message_bulk_set_read',
                           name='api-message-set-read-bulk'),

                       url(r'^messages/unread-count/$',
                           'apps.message.views.get_unread_count',
                           name='api-message-get-unread-count'),

                       url(r'^change-logo/$',
                           'apps.userProfile.views.upload_logo_store', name='api-store-change-logo'),

                        # Include router api
                        url(r'^', include(router.urls)),
                        )