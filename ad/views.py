from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .models import Ad
from .forms import CreateAdForm, AdModifyForm, AdImage_inline_formset, AdLocation_inline_formset
import json
from sorl.thumbnail import get_thumbnail
from datetime import datetime

def _getAdListJson(tags=None, lat=None, lng=None, radius=None):
    object_response = []
    queryset = Ad.objects.all()


    if tags:
        tags = tags.split()
        queryset = queryset.filter(tags__name__in=tags).distinct()
    if lat and lng and radius:
        queryset = queryset.filter(locations__lat__range=(lat - radius, lat + radius))
        queryset = queryset.filter(locations__lng__range=(lng - radius, lng + radius))

    for ad in queryset:
        thumbnail = get_thumbnail(ad.images.first().image, '100x100', crop='center', quality=99).url
        object_response.append( {"title": ad.title + " " + str(datetime.now().strftime('%M:%S')), "body":ad.body, "thumbnail": thumbnail} )
    return json.dumps(object_response)


class SearchAdView(TemplateView):
    def get(self, request, *args, **kwargs):
        tags =  request.GET['tags']
        lat =  float(request.GET['lat'])
        lng =  float(request.GET['lng'])
        radius =  float(request.GET['radius'])

        data = _getAdListJson(tags=tags, lat=lat,  radius=radius, lng=lng)
        return HttpResponse(data, content_type="application/json")

class AdList(TemplateView):
    template_name = "ad/ad-list.html"

    def get_context_data(self, **kwargs):
        data = _getAdListJson()
        return {'json_data': data}

class IndexAdView(ListView):
    template_name = "ad/index.html"
    context_object_name = "ad_list"
    queryset = Ad.objects.all()


class LatestAdView(ListView):
    template_name = "ad/index.html"
    context_object_name = "ad_list"
    queryset = Ad.objects.order_by("created").reverse()[:3]


class DetailAdView(DetailView):
    template_name = "ad/details.html"
    excluded = ('created', '')
    model = Ad


class CreateAdView(CreateView):
    template_name = 'ad/create.html'
    form_class = CreateAdForm
    success_url = '/ad/'
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
    success_url = '/ad/'

    def get_context_data(self, **kwargs):
        context = super(UpdateAdView, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.form_class)

        if self.request.method == 'POST':
            context['images_formset'] = AdImage_inline_formset(self.request.POST, self.request.FILES, instance=self.object)
            context['locations_formset'] = AdLocation_inline_formset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['images_formset'] = AdImage_inline_formset(instance=self.object)
            context['locations_formset'] = AdLocation_inline_formset(instance=self.object)
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
                location_form.instance.title = location_form.cleaned_data.get('title')
                location_form.instance.lat = location_form.cleaned_data.get('lat')
                location_form.instance.lng = location_form.cleaned_data.get('lng')
                location_form.save()
        for location_form in locations_formset.deleted_forms:
            location_form.instance.delete()

        return super(UpdateAdView, self).form_valid(form)
