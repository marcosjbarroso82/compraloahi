from django.conf.urls import patterns, url
from haystack.query import SearchQuerySet

from .views import DetailAdView, AdFacetedSearchView
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

                       # Detail Ad
                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$',
                           DetailAdView.as_view(),
                           name="detail"),

                        )
