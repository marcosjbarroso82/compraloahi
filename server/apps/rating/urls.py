from django.conf.urls import patterns, url

from .views import ActionRatingView

urlpatterns = patterns('',
                       url(r"^(?P<pk>[0-9]+)/$", ActionRatingView.as_view(), name="califications"),
                        )
