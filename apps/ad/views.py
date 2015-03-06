from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect
from haystack.views import FacetedSearchView

from apps.userProfile.models import UserProfile, UserLocation

from .models import Ad
from .forms import CreateAdForm, AdModifyForm, \
    AdImage_inline_formset, AdLocation_inline_formset

from rest_framework import viewsets, filters
from .serializers import AdSerializer


from apps.comment_notification.models import CommentNotification


class AdFacetedSearchView(FacetedSearchView):
    def extra_context(self, **kwargs):
        context = super(AdFacetedSearchView, self).extra_context(**kwargs)

        if (self.request.user.is_authenticated()):
            profile = UserProfile.objects.get(user=self.request.user)
            userLocations = UserLocation.objects.filter(userProfile=profile)
            context['user_locations'] = userLocations
        else:
            context['user_locations'] = {}

        return context


class LatestAdView(ListView):
    template_name = "ad/latest.html"
    context_object_name = "ad_list"
    queryset = Ad.objects.order_by("created").reverse()[:3]


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

    def get_queryset(self):
        return Ad.objects.filter(author= self.request.user)


class AdViewSet(viewsets.ModelViewSet):
    paginate_by = 5
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', 'slug', 'id')

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return Ad.objects.filter(author= self.request.user)
