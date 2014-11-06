from django.conf.urls import patterns, url

from .views import LatestAdView, DetailAdView, CreateAdView, \
    UpdateAdView, AdList, AdDeleteView


urlpatterns = patterns('',
                       url(r'^ad-list/$', AdList.as_view(),
                           name="ad-list"),
                       url(r'^latest/$', LatestAdView.as_view(),
                           name="ad-latest"),
                       url(r'^(?P<pk>\d+)/$',
                           DetailAdView.as_view(), name="ad-detail"),
                       url(r'^create/$', CreateAdView.as_view(),
                           name="ad-create"),
                       url(r'^update/(?P<pk>\d+)/$',
                           UpdateAdView.as_view(), name="ad-update"),
                       url(r'^delete/(?P<pk>\d+)/$',
                           AdDeleteView.as_view(), name="ad-delete"),
                       )
