from django.conf.urls import patterns, include, url
from django.contrib import admin
from ad.views import IndexAdView
from . import settings


urlpatterns = patterns('',
                       url(r'^$', IndexAdView.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^ad/', include("ad.urls", namespace="ad")),
                       url(r'^media/(?P<path>.*)$',
                           "django.views.static.serve",
                           {'document_root': settings.MEDIA_ROOT}),
                       (r'^messages/', include('postman.urls')),

                       )
