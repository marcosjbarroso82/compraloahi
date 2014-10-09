from django import http
#from django.core.urlresolvers import reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Ad
from .forms import CreateAdForm


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
    success_url = '/ad/index/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise http.Http404
        return super(CreateAdView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super(CreateAdView, self).form_valid(form)


class UpdateAdView(UpdateView):
    model = Ad
    fields = ["title", "body"]
    template_name = "ad/update.html"

    def get_object(self):
        return Ad.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return '/ad/' + str(self.object.id)
