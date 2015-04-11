from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, \
    CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from haystack.views import FacetedSearchView
from haystack.query import SearchQuerySet, Clean
from rest_framework import viewsets
from rest_framework import mixins
from django.contrib.gis.measure import *
from django.contrib.gis.geos import Point

from apps.userProfile.models import UserProfile, UserLocation

from .models import Ad
from apps.ad.serializers import SearchResultSerializer, AdSerializer, AdPublicSerializer, AdsSearchSerializer
from .forms import CreateAdForm, AdModifyForm, \
    AdImage_inline_formset, AdLocation_inline_formset
from apps.comment_notification.models import CommentNotification
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json

import logging

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
    #permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AdsSearchSerializer

    def get_queryset(self, *args, **kwargs):
        # Init queryset
        qs = SearchQuerySet().all()
        qs = qs.facet('categories').facet('provinces').facet('localities')

        if self.request.query_params.get('q'):
            #qs = qs.filter_and(title__contains=self.request.query_params.get('q'))
            qs = qs.auto_query(self.request.query_params.get('q'))


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

        self.facets = get_facet(param_facet_url, qs.facet_counts()['fields'].items())

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
        # We delete all Unread Comment Notification for this Ad
        CommentNotification.objects.filter(ad=self.get_object()).delete()
        return super(DetailAdView, self).get(request)


# class ReloadCommentsThread(DetailView):
# Vista que genera un template de la lista de comentarios de un aviso, para poder actualizarla mediante ajax
#     template_name = 'ad/reload-comments.html'
#     model = Ad
#
#     def get(self, request, *args, **kwargs):
#         if kwargs.get('ad_id', None):
#             self.object = Ad.objects.get(pk=kwargs['ad_id'])
#         else:
#             print("ERROR EN LA CLAVE")
#
#         return self.render_to_response(self.get_context_data())


class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/ad/my-ads/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AdDeleteView, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, "Aviso "
                         + self.object.title + " removed success.")
        return HttpResponseRedirect(self.get_success_url())


class CreateAdView(CreateView):
    template_name = 'ad/create.html'
    form_class = CreateAdForm
    # TODO : Redirect to detail ad
    success_url = '/accounts/profile/#/my-ads'
    model = Ad

    def get(self, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        images_form = AdImage_inline_formset()
        locations_form = AdLocation_inline_formset()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                images_form=images_form,
                locations_form=locations_form))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateAdView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        # Images
        images_form = AdImage_inline_formset(
            self.request.POST, self.request.FILES, instance=form.instance)
        # Locations
        locations_form = AdLocation_inline_formset(
            self.request.POST, self.request.FILES, instance=form.instance)

        if (form.is_valid() and images_form.is_valid()):
            return self.form_valid(form, images_form, locations_form)
        else:
            return self.form_invalid(form, images_form, locations_form)

    def form_valid(self, form, images_form, locations_form):
        form.save(commit=False)
        form.instance.author = self.request.user
        form.instance.save()

        # look, validate and save all images
        for image_form in images_form:
            image_form.instance.ad_id = form.instance
            image_form.instance.image = image_form.cleaned_data.get(
                'image')
            if image_form.is_valid() and image_form.instance.image.name:
                image_form.save()

        # look, validate and save all locations
        for location_form in locations_form:
            location_form.instance.ad = form.instance
            location_form.instance.title = image_form.cleaned_data.get('title')
            location_form.instance.lat = image_form.cleaned_data.get('lat')
            location_form.instance.lng = image_form.cleaned_data.get('lng')
            if location_form.is_valid():
                location_form.save()

        return super(CreateAdView, self).form_valid(form)

    def form_invalid(self, form, images_form, locations_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                images_form=images_form,
                locations_form=locations_form))


class UpdateAdView(UpdateView):
    model = Ad
    form_class = AdModifyForm
    template_name = 'ad/update.html'
    # TODO : Redirect to detail ad
    success_url = '/accounts/profile/#/my-ads'

    def get_context_data(self, **kwargs):
        context = super(UpdateAdView, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.form_class)

        if self.request.method == 'POST':
            context['images_formset'] = AdImage_inline_formset(
                self.request.POST, self.request.FILES, instance=self.object)
            context['locations_formset'] = AdLocation_inline_formset(
                self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['images_formset'] = AdImage_inline_formset(
                instance=self.object)
            context['locations_formset'] = AdLocation_inline_formset(
                instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        images_formset = context['images_formset']
        locations_formset = context['locations_formset']
        form.save(commit=False)

        # Images
        for image_form in images_formset:
            if image_form.is_valid():
                image_form.instance.image = image_form.cleaned_data.get(
                    'image')
                if image_form.instance.image.name:
                    image_form.save()
        for image_form in images_formset.deleted_forms:
            image_form.instance.delete()

        # Locations
        for location_form in locations_formset:
            if location_form.is_valid():
                location_form.instance.title = location_form.cleaned_data.get(
                    'title')
                location_form.instance.lat = location_form.cleaned_data.get(
                    'lat')
                location_form.instance.lng = location_form.cleaned_data.get(
                    'lng')
                location_form.save()
        for location_form in locations_formset.deleted_forms:
            location_form.instance.delete()

        return super(UpdateAdView, self).form_valid(form)



class AdUserViewSet(viewsets.ModelViewSet):
    paginate_by = 5
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', 'slug', 'id')

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return Ad.objects.filter(author= self.request.user)
        #return Ad.objects.all()


class AdPublicViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdPublicSerializer

