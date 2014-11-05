from django.conf.urls import patterns, include, url
from django.contrib import admin
from ad.views import IndexAdView
from . import settings


urlpatterns = patterns('',
                        url(r'^$', IndexAdView.as_view()),
                        url(r'^admin/', include(admin.site.urls)),

                        url(r'^ad/', include("ad.urls", namespace="ad")),

                        # Files Media
                        url(r'^media/(?P<path>.*)$',
                           "django.views.static.serve",
                           {'document_root': settings.MEDIA_ROOT}),

                        # Packages Allauth (social authentication)
                        (r'^accounts/', include('allauth.urls')),

                        # My package Profile
                        (r'^accounts/', include('userProfile.urls')),

                        # Package Postman Messages
                        (r'^messages/', include('postman.urls')),

                        (r'^users/', include('user.urls')),

                        # Override package postman
                        (r'^message/', include('message.urls')),

                        # Packages ckeditor
                        (r'^ckeditor/', include('ckeditor.urls')),

                        # Package comments
                        (r'^comments/', include('django_comments_xtd.urls')),


                        (r'^search/', include('haystack.urls')),

                        )
