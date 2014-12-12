from postman.views import WriteView
from postman.models import Message
from .forms import CustomWriteForm

from rest_framework import viewsets, generics
from .serializers import MessageSerializer

from rest_framework_bulk import BulkCreateModelMixin, BulkUpdateModelMixin, BulkDestroyModelMixin, ListBulkCreateUpdateDestroyAPIView

from postman.models import Message

class CustomWriteView(WriteView):
    form_classes=(CustomWriteForm, CustomWriteForm)
    template_name= 'message/write_modal.html'


class MessageList(generics.ListAPIView):

    #queryset = Message.objects.all()
    serializer_class = MessageSerializer
    folder = 'inbox'


    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """

        if self.kwargs['folder'] == 'inbox':
            msgs = Message.objects.inbox(self.request.user)
        elif self.kwargs['folder'] == 'sent':
            msgs = Message.objects.sent(self.request.user)
        elif self.kwargs['folder'] == 'trash':
            msgs = Message.objects.trash(self.request.user)
        elif self.kwargs['folder'] == 'archives':
            msgs = Message.objects.trash(self.request.user)

        return msgs




class MessageBulkViewSet(BulkCreateModelMixin,
                  BulkUpdateModelMixin,
                  BulkDestroyModelMixin,
                  viewsets.ModelViewSet):
    model = Message
    queryset = Message.objects.all()
    serializer_class = MessageSerializer





