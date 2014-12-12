from postman.views import WriteView
from postman.models import Message
from .forms import CustomWriteForm

from rest_framework import viewsets, generics
from .serializers import MessageSerializer


class CustomWriteView(WriteView):
    form_classes=(CustomWriteForm, CustomWriteForm)
    template_name= 'message/write_modal.html'


class MessageList(generics.ListAPIView):

    #queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        return Message.objects.all()