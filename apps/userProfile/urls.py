from django.conf.urls import patterns, url

from .views import UserProfileCreateView, UserProfileDetailView, UserProfileUpdateView, UserProfileModelView


urlpatterns = patterns('',
                       url(r'^profile/create/$',
                           UserProfileCreateView.as_view(),
                           name="create"),
                       url(r'^profile/update/$',
                           UserProfileUpdateView.as_view(),
                           name="update"),
                       url(r'^profile/$',
                           UserProfileDetailView.as_view(),
                           name="detail"),
                       url(r'^ajax-profile/$',
                           UserProfileDetailView.as_view(template_name="userProfile/detail.html"),
                           name="detail-ajax"),
                       url(r'^user-detail/$', UserProfileModelView.as_view()),
                       )
