import string
from django import http
# from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Ad, AdImage
from .forms import CreateAdForm, AdModifyForm, AdImage_inline_formset


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
        return self.render_to_response(
            self.get_context_data(
                form=form,
                images_form=images_form))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateAdView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        images_form = AdImage_inline_formset(
            self.request.POST, self.request.FILES, instance=form.instance)
        if (form.is_valid() and images_form.is_valid()):
            return self.form_valid(form, images_form)
        else:
            return self.form_invalid(form, images_form)

    def form_valid(self, form, images_form):
        form.save(commit=False)
        form.instance.author = self.request.user
        form.instance.save()

        # images_form.save()
        for image_form in images_form:
            image_form.instance.ad_id = form.instance
            image_form.instance.image = image_form.cleaned_data.get(
                'image')
            if image_form.is_valid() and image_form.instance.image.name:
                image_form.save()
        return super(CreateAdView, self).form_valid(form)

    def form_invalid(self, form, images_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                images_form=images_form))


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
        else:
            context['images_formset'] = AdImage_inline_formset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        images_formset = context['images_formset']
        form.save(commit=False)

        for image_form in images_formset:
            if image_form.is_valid():
                image_form.instance.image = image_form.cleaned_data.get('image')
                if image_form.instance.image.name:
                    image_form.save()

        for image_form in images_formset.deleted_forms:
            image_form.instance.delete()


        return super(UpdateAdView, self).form_valid(form)


