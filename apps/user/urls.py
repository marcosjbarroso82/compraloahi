from django.conf.urls import patterns, url

from .views import LogoutView, UserViewSet

urlpatterns = patterns('',
                       url(r'^detail/$',
                           UserViewSet.as_view(),
                           name='users'),
                       url(r'^logout/$',
                           LogoutView.as_view(),
                           name='my-logout'),
                       )


