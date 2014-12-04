from postman.views import WriteView

from .forms import CustomWriteForm


class CustomWriteView(WriteView):
    form_classes=(CustomWriteForm, CustomWriteForm)
    template_name= 'message/write_modal.html'

