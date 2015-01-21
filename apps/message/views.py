from postman.views import WriteView
from postman.models import Message
from .forms import CustomWriteForm

from rest_framework import viewsets, generics, status
from .serializers import MessageSerializer
from rest_framework.views import APIView

from rest_framework.response import Response

from django.db.models import Q

from rest_framework.decorators import api_view
from django.utils.timezone import now as datetime_now

from rest_framework.pagination import PaginationSerializer
from django.core.paginator import Paginator


class CustomWriteView(WriteView):
    form_classes=(CustomWriteForm, CustomWriteForm)
    template_name= 'message/write_modal.html'



class MessageModelViewSet(viewsets.ModelViewSet):
    paginate_by = 5
    serializer_class = MessageSerializer

    def list(self, request, *args, **kwargs):
        self.folder = kwargs.get('folder', None)

        return super(MessageModelViewSet, self).list(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        pass


    def retrieve(self, request, *args, **kwargs):
        """
            Devuelve un thread
        """
        msg = Message.objects.thread(self.request.user, Q(pk=self.kwargs['pk']))
        msg_serializer = MessageSerializer(msg, many=True)
        return Response(msg_serializer.data)


    def get_queryset(self):
        if self.folder:
            if self.folder == 'inbox':
                msgs = Message.objects.inbox(self.request.user)
            elif self.folder == 'sent':
                msgs = Message.objects.sent(self.request.user)
            elif self.folder == 'trash':
                msgs = Message.objects.trash(self.request.user)
            elif self.folder == 'archives':
                msgs = Message.objects.trash(self.request.user)

            return msgs
        else:
            return Message.objects.all()



class MessageDetail(generics.RetrieveAPIView):

    serializer_class = MessageSerializer

    class Meta:
        model = Message

    def get_queryset(self):
        qs = Message.objects.get(pk=self.kwargs['pk'])

        return qs



@api_view(['PATCH'])
def message_bulk_delete(request):
    try:
        for msg in list(request.DATA):
            m = Message.objects.get(pk = msg['id'])
            m.recipient_deleted_at = datetime_now()
            m.save()

        return Response({'menssage': 'ANDA'}, status=status.HTTP_200_OK)
    except:
        return Response({'menssage': 'NO ANDA'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)