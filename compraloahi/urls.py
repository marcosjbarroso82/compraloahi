from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomeView, ApiDashBoardView, DashBoardAjaxView, log
from . import settings_old

from apps.ad import views as adViews
from apps.userProfile.views import UserProfileModelView
from apps.message.views import MessageDetail, MessageModelViewSet
from apps.userProfile.views import UserLocationViewSet
from apps.favorite.views import FavoriteAdViewSet

from rest_framework.routers import DefaultRouter

from apps.user.views import ChangePasswordUpdateAPIView

from rest_framework.authtoken import views

from apps.comment_notification import receivers
from compraloahi import receivers
from compraloahi.views import generate_all_auth_token


router = DefaultRouter()
router.register(r'my-ads', adViews.AdUserViewSet)
router.register(r'ads', adViews.AdPublicViewSet)
router.register(r'user-locations', UserLocationViewSet)
router.register(r'favorites', FavoriteAdViewSet)

router.register(r'ad-search', adViews.SearchViewSet, base_name='search') #/api/v1/ad-search/?q=algo&latitude=-31&longitude=-64&km=33

urlpatterns = patterns('',
                       url(r'^log/', log),
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

                       url(r'^api/v1/messages-all/$',
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
