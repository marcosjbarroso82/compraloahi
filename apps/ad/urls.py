from django.conf.urls import patterns, url
from haystack.query import SearchQuerySet

from .views import DetailAdView, CreateAdView, \
    UpdateAdView, AdDeleteView, AdFacetedSearchView
from .forms import AdSearchForm

from apps.comment_notification import receivers

sqs = SearchQuerySet().facet('categories').facet('localities').facet('provinces')

urlpatterns = patterns('',
                       # List and Search ads with facets
                       url(r'^search/$',
                           AdFacetedSearchView(form_class=AdSearchForm,
                                               searchqueryset=sqs,
                                               template='ad/list.html'),
                           name='search-facet'),



                       # Create Ad
                       url(r'^create/$',
                           CreateAdView.as_view(),
                           name="create"),
                       # Update Ad
                       url(r'^update/(?P<slug>[a-zA-Z0-9_.-]+)/$',
                           UpdateAdView.as_view(),
                           name="update"),
                       # Detele Ad
                       url(r'^delete/(?P<slug>[a-zA-Z0-9_.-]+)/$',
                           AdDeleteView.as_view(),
                           name="delete"),

                       # Detail Ad
                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$',
                           DetailAdView.as_view(),
                           name="detail"),

                       # url(r'^ajax-reload-comments/(?P<ad_id>[\d]+)/$',
                       #      ReloadCommentsThread.as_view(),
                       #      name='valid-message-write'),

                        )
