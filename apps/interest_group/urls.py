from django.conf.urls import patterns, url
from haystack.query import SearchQuerySet

from .views import InterestGroupDetail, InvitationGroup

urlpatterns = patterns('',
                       # Detail Group
                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$',
                           InterestGroupDetail.as_view(),
                           name="detail"),
                       #Invitation
                       url(r'^(?P<group_id>[0-9]+)/(?P<hash>[a-zA-Z0-9]+)/$',
                           InvitationGroup.as_view(),
                           name="invitation"),
                        )
