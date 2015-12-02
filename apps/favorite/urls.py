from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^add-or-remove$', 'apps.favorite.views.add_or_remove', name='toggle'),
    url(r'^remove$', 'apps.favorite.views.remove', name='remove'),
)
