from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from .models import ErrorReport
from django.core.files.base import ContentFile

import base64

@csrf_exempt
def report_error(request):
    if request.POST.get('comment'):
        er = ErrorReport()
        er.description = request.POST.get('comment')

        if request.POST.get('screenshot'):
            format, imgstr = request.POST['screenshot'].split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            er.screenshot = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        er.save()

        return HttpResponse('success', status=200)
    else:
        return HttpResponse('error', status=400)