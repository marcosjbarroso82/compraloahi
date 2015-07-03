from . import models
from rest_framework import serializers

class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Msg

        read_only_fields = ('sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived', 'sender_deleted_at',
                            'recipient_deleted_at', 'sender', 'moderation_status',
                            'parent', 'thread', 'moderation_reason', 'moderation_date')

    def __init__(self, *args, **kwargs):
        action = kwargs['context']['view'].action
        recipient_actions = ['inbox', 'set_read', 'set_trash']
        sender_actions = ['create', 'sent']
        not_allowed = ()

        super(MsgSerializer, self).__init__(*args, **kwargs)

        # Filter fields depending on whether it's a sender or a recipient
        if action in recipient_actions:
            not_allowed = ('sender_archived', 'sender_deleted_at', 'sender',
                           'moderation_status', 'recipient_deleted_at', 'moderation_reason', 'moderation_date')
        elif action in sender_actions:
            not_allowed = ('read_at', 'recipient_archived', 'recipient_deleted_at', 'recipient')

        for field_name in not_allowed:
            self.fields.pop(field_name)
