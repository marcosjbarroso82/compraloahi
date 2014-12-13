from postman.views import WriteView
from postman.models import Message
from .forms import CustomWriteForm

from rest_framework import viewsets, generics
from .serializers import MessageSerializer

from rest_framework.response import Response

from django.db.models import Q


class CustomWriteView(WriteView):
    form_classes=(CustomWriteForm, CustomWriteForm)
    template_name= 'message/write_modal.html'



class MessageModelViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def list(self, request, *args, **kwargs):
        if kwargs['folder'] == 'inbox':
            msgs = Message.objects.inbox(self.request.user)
        elif kwargs['folder'] == 'sent':
            msgs = Message.objects.sent(self.request.user)
        elif kwargs['folder'] == 'trash':
            msgs = Message.objects.trash(self.request.user)
        elif kwargs['folder'] == 'archives':
            msgs = Message.objects.trash(self.request.user)

        msgs_serializer = MessageSerializer(msgs, many=True)

        return Response(msgs_serializer.data)


    def retrieve(self, request, *args, **kwargs):
        """
            Devuelve un thread
        """
        msg = Message.objects.thread(self.request.user, Q(pk=self.kwargs['pk']))
        msg_serializer = MessageSerializer(msg, many=True)
        return Response(msg_serializer.data)


    def get_queryset(self):
        return Message.objects.all()
        #qs = Message.objects.thread(self.request.user, Q(pk=self.kwargs['pk']))
        #return qs


class MessageDetail(generics.RetrieveAPIView):

    serializer_class = MessageSerializer

    class Meta:
        model = Message

    def get_queryset(self):
        qs = Message.objects.get(pk=self.kwargs['pk'])

        return qs

