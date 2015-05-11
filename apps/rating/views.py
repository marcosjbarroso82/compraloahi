from .models import Rating
from django.views.generic import UpdateView
from django.http import HttpResponseNotAllowed
from .forms import RatingForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ActionRatingView(UpdateView):
    model = Rating
    template_name = 'rating/form.html'
    form_class = RatingForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.voter == self.request.user and obj.state == 0:
            return super(ActionRatingView, self).dispatch(request, *args, **kwargs)

        return HttpResponseNotAllowed("No tienes permisos")


    def get_success_url(self):
        obj = self.get_object()
        return reverse('ad:detail', kwargs={'slug': obj.transaction_object.ad.slug})
