from postman.views import WriteView
from postman.models import Message
from .forms import CustomWriteForm

from rest_framework import viewsets, generics, status
from .serializers import MessageSerializer

from rest_framework.response import Response

from django.db.models import Q

from rest_framework.decorators import api_view

from apps.ad.models import Ad
from .models import MessageChannel

from django.utils.timezone import now as datetime_now


class CustomWriteView(WriteView):
    form_classes = (CustomWriteForm, CustomWriteForm)
    template_name = 'message/write_modal.html'


from django.contrib.auth.models import User

class MessageModelViewSet(viewsets.ModelViewSet):
    paginate_by = 10
    serializer_class = MessageSerializer

    def list_all(self, request, *args, **kwargs):
        return super(MessageModelViewSet, self).list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.folder = kwargs.get('folder', None)

        return super(MessageModelViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        sender = request.user
        recipient = None

        if request.POST.get('ad_id'):
            ad = Ad.objects.get(pk=request.POST['ad_id'])
            recipient = ad.author
            mc = MessageChannel(sender=sender, recipient=recipient, ad=ad, date=datetime_now())
            if mc.already_exist():
                mc.save()

        # Sobre escribir si viene especificado ??
        if not recipient and request.POST.get('recipient'):
            recipient = User.objects.get(pk=request.POST['recipient'])

        if request.POST.get('sender'):
            sender = User.objects.get(pk=request.POST['sender'])
        else:
            sender = request.user

        message = Message()
        parent = None
        if request.POST.get('parent'):
            parent = Message.objects.get(pk=request.POST['parent'])
            recipient=parent.sender
            subject = 'RE:' + parent.subject
        if parent and not parent.thread:  # at the very first reply, make it a conversation
            print("first reply")
            parent.thread = parent
            parent.save()
        if parent:
            message.parent = parent
            message.thread = parent.thread
            initial_moderation = message.get_moderation()

        if request.POST.get('subject'):
            subject = request.POST['subject']

        message = Message(subject=subject, body=request.POST['body'], sender=sender, recipient=recipient)
        message.save()
        msg_serializer = MessageSerializer(message, many=False)

        return Response(msg_serializer.data)


    def retrieve(self, request, *args, **kwargs):
        """
            Devuelve un thread
        """

        msg = Message.objects.get(pk=self.kwargs['pk'])
        if msg.read_at is None:
            msg.read_at = datetime_now()
            msg.save()

        Message.objects.set_read(self.request.user, Q(pk=msg.id))

        if msg.thread:
            thread = Message.objects.thread(
                self.request.user, Q(
                    thread=msg.thread))
            msg_serializer = MessageSerializer(thread, many=True)
        else:
            msg_serializer = MessageSerializer([msg], many=True)

        return Response(msg_serializer.data)

    def get_queryset(self):
        if hasattr(self, 'folder'):
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
            m = Message.objects.get(pk=msg['id'])
            m.recipient_deleted_at = datetime_now()
            m.save()

        return Response({'message': 'ANDA'}, status=status.HTTP_200_OK)
    except:
        return Response(
            {'message': 'NO ANDA'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
def message_bulk_set_read(request):
    try:
        for msg in list(request.DATA):
            m = Message.objects.get(pk=msg['id'])
            if m.read_at is None:
                m.read_at = datetime_now()
                m.save()

        return Response({'message': 'ANDA'}, status=status.HTTP_200_OK)
    except:
        return Response(
            {'message': 'NO ANDA'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_valid_message_write(request, *args, **kwargs):
    """
        Valida si un usuario puede contactar al anunciante.
    """
    if kwargs.get('ad_id', None):
        ad = Ad.objects.get(pk=kwargs['ad_id'])

        mc = MessageChannel(sender=request.user, recipient=ad.author, ad=ad,
                            date=datetime_now())

        if mc.already_exist():
            print("no existe")
            return Response({'message': 'OK'}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'message': 'CANAL BLOQUEADO'}, status=status.HTTP_200_OK)
    else:
        return Response(
            {'message': 'CANAL BLOQUEADO'}, status=status.HTTP_200_OK)
    # else:
    #    return Response({'message': 'NEEDLOGIN'}, status=status.HTTP_200_OK)
