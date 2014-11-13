
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from haystack.views import FacetedSearchView


from .models import Ad
from .forms import CreateAdForm, AdModifyForm, \
    AdImage_inline_formset, AdLocation_inline_formset

from django.shortcuts import render_to_response

from .forms import AdSearchForm

class MyFacetedSearchView(FacetedSearchView):
    pass




class AdList(ListView):
    template_name = "ad/list.html"

    def get_context_data(self, **kwargs):
        paginator = Paginator(self.get_queryset(), 10)
        page = self.request.GET.get('page')
        try:
            ads_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            ads_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            ads_list = paginator.page(paginator.num_pages)

        return {'ads_list': ads_list}

    def get_queryset(self):
        queryset = Ad.objects.all()
        if 'tags' in self.request.GET:
            tags = self.request.GET['tags']
            if tags:
                tags = tags.split()
                queryset = queryset.filter(tags__name__in=tags).distinct()
        if self.request.GET.get('lat') and self.request.GET.get('lng') and self.request.GET.get('radius'):
            lat = float(self.request.GET['lat'])
            lng = float(self.request.GET['lng'])
            radius = float(self.request.GET['radius'])

            radius_in_degrees = radius / 111200 # TODO: Need more precision than this
            lat_from = lat - radius_in_degrees
            lat_to = lat + radius_in_degrees
            lng_from = lng - radius_in_degrees
            lng_to = lng + radius_in_degrees

            queryset = queryset.filter(locations__lat__range=(lat_from, lat_to))
            queryset = queryset.filter(locations__lng__range=(lng_from, lng_to))

        return queryset


class LatestAdView(ListView):
    template_name = "ad/latest.html"
    context_object_name = "ad_list"
    queryset = Ad.objects.order_by("created").reverse()[:3]


class DetailAdView(DetailView):
    template_name = "ad/details.html"
    excluded = ('created', '')
    model = Ad


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
    success_url = '/ad/my-ads/'
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
    success_url = '/ad/my-ads/'

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


class AdsByUser(ListView):
    model = Ad
    template_name = 'ad/list-by-user.html'
    context_object_name = "ad_list"
    #queryset = Ad.objects.order_by("created").reverse()[:3]

    def get_queryset(self):
        return Ad.objects.filter(author= self.request.user)