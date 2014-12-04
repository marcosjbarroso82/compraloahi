from tastypie.resources import ModelResource
from apps.ad.models import Ad
from tastypie.authorization import Authorization
from tastypie import fields
from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import SessionAuthentication
from tastypie.paginator import Paginator


class UserObjectsOnlyAuthorization(DjangoAuthorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(author=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.author == bundle.request.user

class AdResource(ModelResource):

    class Meta:
        queryset = Ad.objects.all()
        resource_name = 'ad'

        # user has to be logged in
        authentication = SessionAuthentication()

        authorization = UserObjectsOnlyAuthorization()

        allowed_methods = ['get', 'delete']
        fields = ['title']
        #throttle = BaseThrottle(throttle_at=50)

        paginator_class = Paginator
