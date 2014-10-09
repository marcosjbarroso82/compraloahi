from django.conf.urls import patterns, include, url
from django.contrib import admin
from ad.views import IndexAdView

urlpatterns = patterns('',
                       url(r'^$', IndexAdView.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^ad/', include("ad.urls", namespace="ad")),
                       )
