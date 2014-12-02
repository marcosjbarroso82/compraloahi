from django.conf.urls import patterns, url

from .views import UserProfileCreateView, UserProfileDetailView, UserProfileUpdateView


urlpatterns = patterns('',
                       url(r'^profile/create/$', UserProfileCreateView.as_view(),
                           name="profile-create"),
                       url(r'^profile/update/$', UserProfileUpdateView.as_view(),
                           name="profile-update"),
                       url(r'^profile/$', UserProfileDetailView.as_view(),
                           name="profile-detail"),
                       url(r'^ajax-profile/$', UserProfileDetailView.as_view(template_name="userProfile/detail.html"),
                           name="ajax-profile-detail"),
                       )
