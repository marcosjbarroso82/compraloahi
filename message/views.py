from postman.views import WriteView, ComposeMixin
from django.views.generic import FormView
from .forms import CustomWriteForm

class CustomWriteView(WriteView):
    form_classes=(CustomWriteForm, CustomWriteForm)
    template_name='message/write.html'

