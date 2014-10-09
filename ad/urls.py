from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.IndexAdView.as_view(), name="index"),
    url(r'^latest/$', views.LatestAdView.as_view(), name="latest"),
    url(r'^(?P<pk>\d+)/$', views.DetailAdView.as_view(), name="detail"),
    url(r'^create/$', 'ad.views.create'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^modify/(?P<pk>\d+)/$', views.update.as_view(), name="update"),
    #url(r'^modify/(?P<pk>\d+)/$', 'ad.views.modify'),
)
