#from postman.views import ComposeMixin
from django.views.generic import View

from postman.api import pm_write
from postman.forms import WriteForm

from django.http import HttpResponseRedirect


def writeMessageModal(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/thanks/') # Redirect after POST


class WriteModalView(View):

    def post(self, request, *args, **kwargs):
        pass


