from django.shortcuts import render, redirect

from django.views.generic import CreateView, TemplateView, View

from .models import Interested, CounterWhered
from .forms import RegisterInterestedForm, ContactForm
from django.contrib import messages


class RegisterInterested(CreateView):
    model = Interested
    form_class = RegisterInterestedForm
    success_url = '/dynamic-message/'
    template_name = 'util/interested_form.html'

    def form_valid(self, form):
        response = super(RegisterInterested, self).form_valid(form)
        messages.success(self.request,
            "Te has registrado con exito, ahora enterate de las ultimas novedades. Gracias por confiar en nosotros."
        )
        return response



def register_count_whered(request, whered):
    try:
        obj = CounterWhered.objects.get(whered=whered)
        obj.counter += 1
        obj.save()
    except CounterWhered.DoesNotExist:
        CounterWhered(whered=whered, counter=1).save()

    return redirect('/')


class TemplateMessage(TemplateView):
    template_name = 'util/messages_template.html'


from django.views.generic.edit import FormView

class ContactFormView(FormView):
    template_name = 'util/contact.html'
    form_class = ContactForm
    success_url = '/dynamic-message/'

    def form_valid(self, form):
        response = super(ContactFormView, self).form_valid(form)
        messages.success(self.request,
            "Hemos recibido tu mensaje, nos estaremos comunicando a la brevedad.."
        )
        form.send_email()
        return response

