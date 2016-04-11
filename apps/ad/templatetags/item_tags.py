# From http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/#comment-1193609278
from django import template

from django.template import Library, Node, resolve_variable

from apps.ad.models import Ad
from haystack.query import SearchQuerySet

from django.contrib.gis.measure import D
#from haystack.utils.geo import Point, D
from django.contrib.gis.geos import Point

register = template.Library()
 
@register.assignment_tag
def get_near_items(item):
    #import ipdb; ipdb.set_trace()
    qs = SearchQuerySet().all()
    loc = item.locations.first()
    point = Point(loc.lng, loc.lat)
    qs.dwithin('location', point, D(m=50000)).distance('location', point)

    return qs


