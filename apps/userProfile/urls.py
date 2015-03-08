from django.conf.urls import patterns, url

from .views import UserProfileCreateView, UserProfileDetailView


urlpatterns = patterns('',
                       url(r'^profile/create/$',
                           UserProfileCreateView.as_view(),
                           name="create"),
                       # Url to open dashboard
                       url(r'^profile/$',
                           UserProfileDetailView.as_view(),
                           name="detail"),
                       # url(r'^ajax-profile/$',
                       #     UserProfileDetailView.as_view(template_name="userProfile/detail.html"),
                       #     name="detail-ajax")
                       )
