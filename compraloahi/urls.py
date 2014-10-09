from django.conf.urls import patterns, include, url
from django.contrib import admin
from ad.views import IndexAdView

urlpatterns = patterns('',
    # Examples:
     url(r'^$', IndexAdView.as_view()),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ad/', include("ad.urls", namespace="ad")),
)
