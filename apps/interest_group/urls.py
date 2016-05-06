from django.conf.urls import patterns, url
from haystack.query import SearchQuerySet

from .views import InterestGroupDetail

urlpatterns = patterns('',
                       # Detail Ad
                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$',
                           InterestGroupDetail.as_view(),
                           name="detail"),

                        )
