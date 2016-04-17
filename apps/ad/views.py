import json
import logging

from django.contrib.gis.measure import D
#from haystack.utils.geo import Point, D
from django.contrib.gis.geos import Point
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import DetailView

from haystack.views import FacetedSearchView
from haystack.query import SearchQuerySet

from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.parsers import FileUploadParser

from apps.rating.models import OverallRating
from apps.userProfile.models import UserProfile, UserLocation

from .models import Ad, Category, AdImage
from .serializers import SearchResultSerializer, AdSerializer, AdPublicSerializer, AdsSearchSerializer, \
    CategorySerializer, ImageSerializer
from rest_framework import status
from apps.notification.models import Notification
from rest_framework.decorators import list_route, detail_route, parser_classes


logger = logging.getLogger('debug')

# Devolver un diccionario de filtros activos y un array de facets detallados
def get_facet(params_url, facets_fields):
    print(30*"==FACET==")
    print(params_url)
    print(facets_fields)
    # Var to all facets active
    facets_active = {}
    # Var to all facets
    facets = []
    for name, values in facets_fields:
        facet = {}
        facet['name'] = name
        facet['values'] = []
        facet['activated'] = False

        facet_active = {}
        if not facet['activated']:
            for param_facet in params_url:
                param_name = str(param_facet).split(':')[0]
                # Valida si el parametro pertenece a un facet, y si el facet mismo ya esta activo
                if param_name.split('_')[0] == name and facets_active.get(param_name.split('_')[0], True):
                    if param_name.split('_')[1] != 'exact':
                         break
                    param_value = str(param_facet).split(':')[1]
                    facet_active['value'] = param_value
                    facet_active['name'] = param_name.split('_')[0]
                    break

        for value in values:
            val = {}
            val['name'] = value[0]
            val['cant'] = value[1]
            val['activated'] = False

            if not facet['activated'] and facet_active.get('value', None):
                if val['name'] == facet_active['value']:
                    facets_active[facet_active['name']] = facet_active['value']
                    facet['activated'] = True
                    val['activated'] = True
                    if facet['name'] == 'categories':
                        try:
                            val['label'] = Category.objects.get(slug=val['name']).name
                        except:
                            val['label'] = val['name']

            facet['values'].append(val)

        facets.append(facet)

    return facets


class SearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AdsSearchSerializer

    def get_queryset(self, *args, **kwargs):
        # Init queryset
        qs = SearchQuerySet().all()
        qs = qs.facet('categories')

        if self.request.query_params.get('q'):
            #qs = qs.filter_and(title__contains=self.request.query_params.get('q'))
            qs = qs.auto_query(self.request.query_params.get('q'))

        distance = None
        try:
            for k,v in self.request.query_params.items():
                if k in D.UNITS.keys():
                    distance = {k:v}

        except Exception as e:
            logging.error(e)

        point = None

        #import pdb; pdb.set_trace()
        try:
            print(30*"LAT===")
            print(float(self.request.query_params['lat']))
            print(30*"=LNG=")
            print(float(self.request.query_params['lng']))
            point = Point(float(self.request.query_params['lng']), float(self.request.query_params['lat']))
        except Exception as e:
            logging.error(e)

        #import ipdb; ipdb.set_trace()
        if distance and point:
            qs = qs or SearchQuerySet()
            qs = qs.dwithin('location', point, D(**distance)).distance('location', point)

        try:
            if self.request.query_params.get('w') and self.request.query_params.get('s')\
                    and self.request.query_params.get('n') and self.request.query_params.get('e'):
                bottom_left = Point( float( self.request.query_params['w'] ), float( self.request.query_params['s']) )
                top_right = Point( float(self.request.query_params['e']), float( self.request.query_params['n']) )
                qs = qs.within('location', bottom_left, top_right)
            #else:
        except:
            pass

        try:
            param_facet_url = list(self.request.query_params.getlist('selected_facets', []))
        except:
            param_facet_url = list(self.request.query_params.get('selected_facets', []))

        for facet in param_facet_url:
            if ":" not in facet:
                continue
            field, value = facet.split(":", 1)
            if value and field.split('_')[1] == 'exact':
                qs = qs.narrow('%s:"%s"' % (field, qs.query.clean(value)))
        try:
            self.facets = get_facet(param_facet_url, qs.facet_counts()['fields'].items())
        except:
            self.facets = []

        order_by = self.request.query_params.get('order_by')
        if order_by:
            if order_by is 'distance':
                if distance and point:
                    qs = qs.order_by(self.request.query_params.get('order_by'))
            else:
                qs = qs.order_by(self.request.query_params.get('order_by'))

        return qs

    def list(self, request, *args, **kwargs):
        ads = self.get_queryset()
        paginated_by = 10
        paginator = Paginator(ads, paginated_by)
        page = self.request.query_params.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page
            page = 1
            results = paginator.page(page)
        except EmptyPage:
            # If page is out of range, deliver last page
            page = paginator.num_pages
            results = paginator.page(paginator.page)

        results.page = page
        results.facets = self.facets
        results.count = paginator.count
        results.paginated_by = paginated_by

        if results.has_next():
            results.next = results.next_page_number()
        else:
            results.next = None

        if results.has_previous():
            results.previous = results.previous_page_number()
        else:
            results.previous = None

        result_serializer = SearchResultSerializer(instance=results, context={"request": request})

        return Response(result_serializer.data)


class AdFacetedSearchView(FacetedSearchView):
    def extra_context(self, **kwargs):
        context = super(AdFacetedSearchView, self).extra_context(**kwargs)

        if (self.request.user.is_authenticated()):
            profile = UserProfile.objects.get(user=self.request.user)
            userLocations = UserLocation.objects.filter(userProfile=profile)
            context['user_locations'] = userLocations
        else:
            context['user_locations'] = {}

        # TODO Se esta creando el json de facets antes de setearlo y las cantidades quedan mal generadas.
        try:
            param_facet_url = list(self.request.GET.getlist('selected_facets', []))
        except:
            param_facet_url = list(self.request.GET.get('selected_facets', []))

        self.facets = get_facet(param_facet_url, self.searchqueryset.facet_counts()['fields'].items())

        context['clean_facets'] = json.dumps(self.facets)
        context['q'] = self.request.GET.get('q', '')
        return context


class IsAdImageIsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.ad.author == request.user:
            return True
        return False


class AdImageModelViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permissions_class = (IsAdImageIsUser, )
    #parser_classes = (FileUploadParser, )

    def get_queryset(self):
        return AdImage.objects.filter(ad__author=self.request.user.pk)

    @parser_classes((FileUploadParser,))
    def create(self, request, *args, **kwargs):
        return super(AdImageModelViewSet, self).create(request, *args, **kwargs)

    #def destroy(self, request, *args, **kwargs):
        #if json.loads(request.data.get('data')).get('secure'):
        #    return super(AdImageModelViewSet, self).destroy(request, *args, **kwargs)
        #else:
        # try:
        #     img = self.get_object().get(pk=kwargs['pk'])
        #     if AdImage.objects.filter(ad=img.ad).count() > 1:
        #         return self.destroy(request, *args, **kwargs)
        #     else:
        #         return Response({"message": "Error, the ad required a image. Add other image and before remove this."}, status=status.HTTP_400_BAD_REQUEST)
        # except AdImage.DoesNotExist:
        #     return Response({"message": "Error"}, status=status.HTTP_401_UNAUTHORIZED)
        # except:
        #     return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)


class AdUserViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def destroy(self, request, pk=None):
        try:
            ad = Ad.objects.get(pk=pk, author=request.user.pk)
            ad.status = 0
            ad.save()
            return Response({'message': 'Success deleted'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user).exclude(status=0)


class AdPublicViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdPublicSerializer
    permission_classes = (AllowAny,)
    paginate_by = 10


class CategoriesListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



class DetailAdView(DetailView):
    template_name = "ad/details.html"
    excluded = ('created', '')
    model = Ad
    context_object_name = 'item'

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        if ad.author == request.user:
            for notification in Notification.objects.filter(receiver=ad.author, type='cmmt', read=None):
                notification.marked_read()
        return super(DetailAdView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(DetailAdView, self).get_context_data(**kwargs)
        try:
            context['rating'] = OverallRating.objects.get(user=context['item'].author).rate
        except OverallRating.DoesNotExist:
            context['rating'] = ""
        try:
            context['comments_limit'] = int(self.request.GET.get('comments_limit', '') )
        except:
            context['comments_limit'] = 5
        return context