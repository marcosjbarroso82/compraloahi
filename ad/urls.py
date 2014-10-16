from django.conf.urls import patterns, url

from .views import LatestAdView, DetailAdView, CreateAdView, IndexAdView, \
    UpdateAdView, SearchAdView


urlpatterns = patterns('',
                       url(r'^$', IndexAdView.as_view(), name="index"),
                       url(r'^latest/$', LatestAdView.as_view(),
                           name="latest"),
                       url(r'^(?P<pk>\d+)/$',
                           DetailAdView.as_view(), name="detail"),
                       url(r'^create/$', CreateAdView.as_view(),
                           name="ad-create"),
                       url(r'^modify/(?P<pk>\d+)/$',
                           UpdateAdView.as_view(), name="update"),
                       url(r'^search/$', SearchAdView.as_view(),
                           name="latest"),
                       )
