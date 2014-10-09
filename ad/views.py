from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.views import generic


from .models import Ad
from .forms import AdCreateForm, AdModifyForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.context_processors import csrf

class IndexAdView(generic.ListView):
    template_name = "ad/index.html"
    context_object_name = "ad_list"
    queryset = Ad.objects.all()

class LatestAdView(generic.ListView):
    template_name = "ad/latest.html"
    context_object_name = "ad_list"
    queryset = Ad.objects.order_by("created").reverse()[:3]

class DetailAdView(generic.DetailView):
    template_name = "ad/details.html"
    model = Ad

def create(request):
    if request.POST:
        form = AdCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("ad:index"))
    else:
        form = AdCreateForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form
    return render_to_response('ad/create_ad.html', args)


class update(generic.UpdateView):
    model = Ad
    fields = ["title", "body"]
    template_name = "ad/update.html"

    #success_url = reverse_lazy("ad:detail", kwargs={'pk': pk})
    def get_object(self):
        #return Ad.objects.get(pk=self.request.GET.get('pk'))
        #return Ad.objects.get(pk=self.request.GET.get('pk',None))
        return Ad.objects.get(pk=self.kwargs['pk'])
        #return CustomUser.objects(id=self.kwargs['pk'])[0]

    def get_success_url(self):
        return '/ad/' + str(self.object.id)


"""
def modify(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.POST:
        form = AdModifyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("ad:index"))
    else:
        data = {'title' : ad.title, "body": ad.body}
        form = AdModifyForm(initial=data)

    args = {
    }

    args.update(csrf(request))
    args['form'] = form
    return render_to_response('ad/modify_ad.html', args)
"""