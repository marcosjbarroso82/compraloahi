from . import models
from rest_framework import serializers


class MsgSerializer(serializers.ModelSerializer):
    is_new = serializers.BooleanField(required=False)
    sender_deleted = serializers.BooleanField(required=False)
    recipient_deleted = serializers.BooleanField(required=False)
    is_replied = serializers.BooleanField(read_only=True)

    class Meta:
        # list_serializer_class = MsgListSerializer
        model = models.Msg
        read_only_fields = ('sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived',
                            'sender_deleted_at', 'sender_deleted', 'is_new', 'recipient_deleted',
                            'recipient_deleted_at', 'moderation_status', 'moderation_reason',
                            'moderation_date')

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

        for field_name in not_allowed_to_show:
            self.fields.pop(field_name)