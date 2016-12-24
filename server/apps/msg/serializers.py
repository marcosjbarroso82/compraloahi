from . import models
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail
from apps.ad.serializers import AdPublicSerializer

from apps.ad.models import Ad

class MsgSerializer(serializers.ModelSerializer):
    is_new = serializers.SerializerMethodField()
    sender_deleted = serializers.BooleanField(required=False)
    recipient_deleted = serializers.BooleanField(required=False)
    is_replied = serializers.BooleanField(read_only=True)
    related_obj = serializers.SerializerMethodField()
    object_id = serializers.IntegerField(write_only=True, min_value=0)

    def validate_object_id(self, value):
        try:
            Ad.objects.get(pk=value)
        except:
            raise serializers.ValidationError("The item id is incorrect")

        return value

    class Meta:
        # list_serializer_class = MsgListSerializer
        model = models.Msg
        read_only_fields = ('sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived',
                            'sender_deleted_at', 'sender_deleted', 'is_new', 'recipient_deleted',
                            'recipient_deleted_at', 'moderation_status', 'moderation_reason',
                            'moderation_date', 'related_obj')
        write_only_fields = ('object_id',)
        exclude = ('content_type',)

    def __init__(self, *args, **kwargs):
        super(MsgSerializer, self).__init__(*args, **kwargs)
        user = kwargs['context']['request'].user
        action = self.context['view'].action

        # Filter fields depending on whether it's a sender or a recipient
        not_allowed_to_show = ()
        user_type = None
        # raise Exception(action)
        try:
            if action == 'inbox' or action == 'list' or action == 'trash' or user == self.instance.recipient:
                user_type = 'recipient'
            elif action == 'sent' or user == self.instance.sender:
                user_type = 'sender'
            else:
                raise Exception("User is neither sender nor recipient")
        except:
            # TODO: if its an empty list, it fails
            # TODO: change this
            user_type = 'sender'

        if user_type == 'recipient':
            not_allowed_to_show = ('recipient', 'sender_archived', 'sender_deleted_at', 'sender', 'sender_deleted',
                                   'moderation_status', 'moderation_reason', 'moderation_date')
        elif user_type == 'sender':
            not_allowed_to_show = ( 'read_at', 'replied_at', 'is_replied', 'recipient_deleted',
                                    'recipient_archived', 'recipient_deleted_at')
            self.fields['recipient'].write_only = True

        if action == 'create' or action == 'reply':
            self.fields['is_new'].read_only = True
            self.fields['sender_deleted'].read_only = True
            self.fields['recipient_deleted'].read_only = True
        else:
            self.fields['subject'].read_only = True
            self.fields['body'].read_only = True

        if action == 'reply':
            self.fields['object_id'].read_only = True
            self.fields['object_id'].required = False

        for field_name in not_allowed_to_show:
            self.fields.pop(field_name)


    def get_related_obj(self, obj):
        if obj.related_obj:
            ad = obj.related_obj
            image = ad.images.all().filter(default=True).first()
            ad_serializer = {
                'id': ad.id,
                'images': [
                    {'thumbnail_110x110': get_thumbnail(image, '110x110', crop='center', quality=99).url if image else '' }
                ],
                'title': ad.title
            }
            return ad_serializer
        else:
            return {}

    def get_is_new(self, obj):
        request = self.context.get('request', None)
        if request is not None:
            # TODO: Resuelve el problema de cuando se accede a un trhread el usuario que envio el mensaje no debe saber
            # si el mensaje es nuevo, osea, el mensaje esta leido o no leido. En el caso que el sender entra al detalle
            # del mensaje el atributo is_new es False
            if request.user == obj.sender:
                return False
            else:
                return obj.is_new
