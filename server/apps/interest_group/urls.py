from django.conf.urls import patterns, url
from haystack.query import SearchQuerySet

from .views import InterestGroupDetail, InvitationGroup, JoinGroup

urlpatterns = [
    # Detail Group
    url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$',
        InterestGroupDetail.as_view(),
        name="detail"),

    #Join
    url(r'^(?P<group_id>[0-9]+)/join/$',
        JoinGroup.as_view(),
        name="join-group"),
    #Invitation
    url(r'^(?P<group_id>[0-9]+)/(?P<hash>[a-zA-Z0-9]+)/$',
        InvitationGroup.as_view(),
        name="invitation"),

    ]
