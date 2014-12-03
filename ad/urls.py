from django.conf.urls import patterns, url

from haystack.query import SearchQuerySet

from .views import LatestAdView, DetailAdView, CreateAdView, \
    UpdateAdView, AdDeleteView, AdsByUser, AdFacetedSearchView

from .forms import AdSearchForm

sqs = SearchQuerySet().facet('categories').facet('localities').facet('provinces')

urlpatterns = patterns('',
                       # List and Search ads
                       url(r'^ad-list/$', AdFacetedSearchView(form_class=AdSearchForm, searchqueryset=sqs, template='ad/list.html'), name='my_facet_search_view'),
                       # Latest ads
                       url(r'^latest/$', LatestAdView.as_view(),
                           name="ad-latest"),
                       # Create Ad
                       url(r'^create/$', CreateAdView.as_view(),
                           name="ad-create"),
                       # Update Ad
                       url(r'^update/(?P<pk>\d+)/$',
                           UpdateAdView.as_view(),
                           name="ad-update"),
                       # Detele Ad
                       url(r'^delete/(?P<pk>\d+)/$',
                           AdDeleteView.as_view(),
                           name="ad-delete"),
                       url(r'^my-ads/$', AdsByUser.as_view(),
                           name="ad-by-user"),
                        # Detail Ad
                       url(r'^(?P<pk>\d+)/$',
                           DetailAdView.as_view(),
                           name="ad-delete"),
                       #url(r'^ajax-table-ads-by-user/$', AdsByUser.as_view(template_name='userProfile/table_ads_by_user.html'), name="ajax-table-ad-by-user"),
                       url(r'^ajax-table-ads-by-user/$', AdsByUser.as_view(template_name='userProfile/table_ads_by_user.html'), name="ajax-table-ad-by-user"),

                        )
