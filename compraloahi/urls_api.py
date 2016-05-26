from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from apps.ad.views import AdUserViewSet, AdPublicViewSet, SearchViewSet, CategoriesListAPIView, AdImageModelViewSet
from apps.favorite.views import FavoriteAdViewSet
from apps.notification.views import NotificationListApiView, NotificationRetrieveApiView, \
    RegisterGCMNotification, UnregisterGCMNotification, NotificationMarkBulkReadApiView, ConfigNotificationModelViewSet
from apps.user.views import ChangePasswordUpdateAPIView
from apps.userProfile.views import UserLocationViewSet, UserProfileModelView, StoreModelViewSet, \
    ProfileLocationViewSet, ConfigPrivacityViewSet
from apps.msg.views import MsgViewSet
from apps.user.views import FacebookLogin, GoogleLogin
from apps.comments.views import ThreadedCommentViewSet
from apps.interest_group.views import InterestGroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'user-items', AdUserViewSet, base_name='ad-by-user')
router.register(r'user-items-images', AdImageModelViewSet, base_name='ad-images')
router.register(r'items', AdPublicViewSet, base_name='ads')
router.register(r'user-locations', UserLocationViewSet, base_name='location-by-user')
router.register(r'favorites', FavoriteAdViewSet, base_name='favorites')
router.register(r'item-search', SearchViewSet, base_name='search') #/ad-search/?q=algo&latitude=-31&longitude=-64&km=33
router.register(r'msgs', MsgViewSet, base_name='msgs')
router.register(r'comments', ThreadedCommentViewSet, base_name='comment_api')
router.register(r'interest-groups', InterestGroupViewSet, base_name='interest_group_api')
router.register(r'(?P<group_pk>\d+)/post', PostViewSet, base_name='timeline')

urlpatterns = patterns('',
                       ## START URL ACTUALIZADAS TODO: ESTAS URL SE PASARON AHORA, ACOMODAR EL CLIENTE:
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

                        ### END URL ACTUALIZADAS
                       url(r'^categories/$', CategoriesListAPIView.as_view(), name='categories'),

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
                       #url(r'^api-generate-all-token-auth/', generate_all_auth_token),

                       url(r'^api-token-auth/', obtain_auth_token),

                       # Config user privacity
                       url(r'^config-privacity/$', ConfigPrivacityViewSet.as_view({'get': 'retrieve', 'put': 'update'})),

                       # Update Address profile
                       url(r'^profile/address/$', ProfileLocationViewSet.as_view({'get': 'retrieve', 'put': 'update'})),

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

                       url('^store-name-is-unique/(?P<slug>.+)/$',
                           'apps.userProfile.views.store_name_is_unique',
                           name='api-user-store-name-is-unique'),

                       # Login and logout (DjangoRestFramework)
                       url(r'^',
                           include('rest_framework.urls',
                                   namespace='rest_framework')),

                       url(r'^change-logo/$',
                           'apps.userProfile.views.upload_logo_store', name='api-store-change-logo'),

                        # Include router api
                        url(r'^', include(router.urls)),
                        )