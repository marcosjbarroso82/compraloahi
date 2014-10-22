from django.conf.urls import patterns, url

from .views import UserProfileCreateView, UserProfileDetailView, UserProfileUpdateView


urlpatterns = patterns('',
                       url(r'^profile/create/$', UserProfileCreateView.as_view(), name="profile-create"),
                       url(r'^profile/edit/$', UserProfileUpdateView.as_view(),
                           name="profile-edit"),
                       url(r'^profile/$', UserProfileDetailView.as_view(),
                           name="profile-detail"),
                       )
