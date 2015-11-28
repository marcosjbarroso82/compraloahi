from django.shortcuts import render

from django.views.generic import CreateView

from .models import Interested
from .forms import RegisterInterestedForm


class RegisterInterested(CreateView):
    model = Interested
    form_class = RegisterInterestedForm
    success_url = '/success/'
    template_name = 'index.html'