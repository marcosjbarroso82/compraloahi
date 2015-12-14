from django import forms

from haystack.forms import FacetedSearchForm
from haystack.utils.geo import Point, D


class AdSearchForm(FacetedSearchForm):
    lat = forms.FloatField(required=False, label="lat")
    lng = forms.FloatField(required=False, label="lng")
    radius = forms.FloatField(required=False, label="radius")

    selected_facets = forms.CharField(required=False, widget=forms.HiddenInput)
    order_by = forms.CharField(required=False, widget=forms.HiddenInput)

    def no_query_found(self):
        return self.searchqueryset.all()

    def search(self):
        # First, store the SearchQuerySet received from other processing. (the main work is run internally by Haystack here).
        sqs = super(AdSearchForm, self).search()
        try:
            if self.cleaned_data.get('lat') and self.cleaned_data.get('lng') and self.cleaned_data.get('radius'):
                location = Point(self.cleaned_data.get('lng'), self.cleaned_data.get('lat'))
                max_dist = D(km=self.cleaned_data.get('radius')) # Un bug en haystack demanda que se multiplique por 1000. asique ahi lo esta tomando en metros
                sqs = sqs.dwithin('location', location, max_dist)

            if self.cleaned_data.get('order_by'):
                # TODO: Add support for multiple order fields
                # TODO: Add support for non-numeric field ordering ( so far only "pride" and pub_date" are working)
                order_by = self.cleaned_data.get('order_by')
                # if Search Query Set is order by distance, it might no be secure to order by any other field ( accordind to the hasytack codmumentation )
                if ( (order_by == 'distance' or order_by == '-distance')) and self.cleaned_data.get('lat') and self.cleaned_data.get('lng'):
                    location = Point(self.cleaned_data.get('lng'), self.cleaned_data.get('lat'))
                    sqs = sqs.distance('location', location).order_by(order_by)
                else:
                    sqs = sqs.order_by(order_by )

        except:
            pass
        # if something goes wrong
        if not self.is_valid():
            return self.no_query_found()

        return sqs

    def __name__(self):
        return "AdSearchForm"