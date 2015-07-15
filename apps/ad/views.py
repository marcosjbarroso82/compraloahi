import json
import logging

from django.contrib.gis.measure import *
from django.contrib.gis.geos import Point
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import DetailView

from haystack.views import FacetedSearchView
from haystack.query import SearchQuerySet

from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from apps.rating.models import OverallRating
from apps.userProfile.models import UserProfile, UserLocation
from apps.adLocation.models import AdLocation

from .models import Ad, Category, AdImage
from .serializers import SearchResultSerializer, AdSerializer, AdPublicSerializer, AdsSearchSerializer, CategorySerializer, AdLocationSerializer
from rest_framework import status


logger = logging.getLogger('debug')

# Devolver un diccionario de filtros activos y un array de facets detallados
def get_facet(params_url, facets_fields):
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

            facet['values'].append(val)

        facets.append(facet)

    return facets


class SearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AdsSearchSerializer

    def get_queryset(self, *args, **kwargs):
        # Init queryset
        qs = SearchQuerySet().all()
        qs = qs.facet('categories').facet('provinces').facet('localities')

        if self.request.query_params.get('q'):
            #qs = qs.filter_and(title__contains=self.request.query_params.get('q'))
            qs = qs.auto_query(self.request.query_params.get('q'))


        distance = None
        try:
            for k,v in self.request.QUERY_PARAMS.items():
                if k in D.UNITS.keys():
                    distance = {k:v}

        except Exception as e:
            logging.error(e)
        point = None

        try:
            point = Point(float(self.request.QUERY_PARAMS['lng']), float(self.request.QUERY_PARAMS['lat']))
        except Exception as e:
            logging.error(e)

        if distance and point:
            qs = qs or SearchQuerySet()
            qs = qs.dwithin('location', point, D(**distance)).distance('location', point)

        try:
            bottom_left = Point( float( self.request.QUERY_PARAMS['w'] ), float( self.request.QUERY_PARAMS['s']) )
            top_right = Point( float(self.request.QUERY_PARAMS['e']), float( self.request.QUERY_PARAMS['n']) )
            qs = qs.within('location', bottom_left, top_right)
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

        paginator = Paginator(ads, 10)
        page = self.request.query_params.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page
            results = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page
            results = paginator.page(paginator.num_pages)

        results.facets = self.facets
        results.count = paginator.count

        if results.has_next():
            results.next = results.next_page_number()
        else:
            results.next = None

        if results.has_previous():
            results.previous = results.previous_page_number()
        else:
            results.previous = None

        result_serializer = SearchResultSerializer(instance=results)

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


class DetailAdView(DetailView):
    template_name = "ad/details.html"
    excluded = ('created', '')
    model = Ad

    def get(self, request, *args, **kwargs):
        return super(DetailAdView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(DetailAdView, self).get_context_data(**kwargs)
        try:
            context['rating'] = OverallRating.objects.get(user=context['ad'].author).rate
        except OverallRating.DoesNotExist:
            context['rating'] = ""
        try:
            context['comments_limit'] = int(self.request.GET.get('comments_limit', '') )
        except:
            context['comments_limit'] = 5
        return context


class AdUserViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('title', 'slug', 'id')
    parser_classes = (MultiPartParser, FormParser, FileUploadParser )

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return Ad.objects.filter(author= self.request.user)

    def create(self, request, *args, **kwargs):
        if request.data and request.data.get('data') and len(request.FILES) > 0:

            ad_data = json.loads(request.data.get('data'))
            ad_data['author'] = request.user.id
            ad_serializer = AdSerializer(data=ad_data)

            if ad_serializer.is_valid():
                ad_serializer.save()
                location_serializer = {}
                for location_data in ad_data['locations']:
                    location_data['ad'] = ad_serializer.instance.id
                    location_serializer = AdLocationSerializer(data=location_data)
                    location_serializer.run_validation(location_data)

                    try:
                        if location_serializer.is_valid():
                            location_serializer.save()
                        else:
                            raise Exception
                    except:
                        ad_serializer.instance.delete()
                        return Response({"Error al intentar guardar la ubicacion"},
                                        status=status.HTTP_400_BAD_REQUEST)

                images = []
                try:
                    # TODO: Whats happen if any images set default or more to one images are default?
                    for image_data in ad_data['images']:
                        for key, image in request.FILES.items():
                            if image_data['name'] == image.name:
                                images.append(AdImage(image=image, ad_id=ad_serializer.instance,
                                                      default=image_data.get('default', False)).save())
                                break
                except:
                    ad_serializer.instance.delete()
                    location_serializer.instance.delete()
                    for img in images:
                        img.delete()

                    return Response({"Error al intentar guardar las imagenes"},
                                    status=status.HTTP_400_BAD_REQUEST)

                return Response({'message': "SUCCESS"})
            else:
                ad_serializer.run_validation(ad_data)

        return Response({'message': "ERROR"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        if request.data and request.data.get('data'):
            ad_data = json.loads(request.data.get('data'))
            ad_data['author'] = request.user.id
            try:
                ad = Ad.objects.get(id= ad_data.get('id'))
                ad_serializer = AdSerializer(data=ad_data, instance=ad)

                if ad_serializer.is_valid():
                    ad_serializer.save()
                    for location_data in ad_data['locations']:
                        try:
                            ad_location = AdLocation.objects.get(id= location_data.get('id'))
                            location_data['ad'] = ad_serializer.instance.id
                            location_serializer = AdLocationSerializer(data=location_data,
                                                                       instance=ad_location)
                            location_serializer.run_validation(location_data)
                            try:
                                if location_serializer.is_valid():
                                    location_serializer.save()
                                else:
                                    raise Exception
                            except:
                                raise Exception
                        except:
                            return Response({"Error al intentar guardar la ubicacion"},
                                            status=status.HTTP_400_BAD_REQUEST)

                    # TODO: Whats happen if images change default or any images set default?
                    if len(request.FILES) > 0:
                        try:

                            for image_data in ad_data['images']:
                                if not image_data.get('deleted', False) or image_data.get('is_new', False) \
                                        and image_data.get('name'):
                                    for key, image in request.FILES.items():
                                        if image_data.get('name', '') == image.name:
                                            AdImage(image=image, ad_id=ad_serializer.instance,
                                                    default=image_data.get('default', False)).save()
                                            break
                                else:
                                    if image_data.get('deleted'):
                                        try:
                                            AdImage.objects.get(id=image_data.get('id')).delete()
                                        except AdImage.DoesNotExist:
                                            pass

                        except:
                            return Response({"Error al intentar guardar las imagenes"},
                                            status=status.HTTP_400_BAD_REQUEST)

                    return Response({'message': "SUCCESS"})
                else:
                    ad_serializer.run_validation(ad_data)
            except Ad.DoesNotExist:
                return Response({'message': "The ad instance doesnt exist"},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': "ERROR"}, status=status.HTTP_400_BAD_REQUEST)


class AdPublicViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdPublicSerializer
    permission_classes = (AllowAny,)
    paginate_by = 10


class CategoriesListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
