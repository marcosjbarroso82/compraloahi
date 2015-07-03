from . import models
from rest_framework import serializers
class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Msg

        read_only_fields = ('sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived', 'sender_deleted_at',
                            'recipient_deleted_at', 'sender', 'moderation_status',
                            'parent', 'thread', 'moderation_reason', 'moderation_date')

    def __init__(self, *args, **kwargs):
        super(MsgSerializer, self).__init__(*args, **kwargs)
        user = kwargs['context']['request'].user

        # Filter fields depending on whether it's a sender or a recipient
        not_allowed = ()
        if  user == self.instance.recipient:
            print("Im the recipient")
            not_allowed = ('sender_archived', 'sender_deleted_at', 'sender',
                           'moderation_status', 'recipient_deleted_at', 'moderation_reason', 'moderation_date')
        elif user == self.instance.sender:
            print("Im the sender")
            not_allowed = ('read_at', 'recipient_archived', 'recipient_deleted_at', 'recipient')

        for field_name in not_allowed:
            self.fields.pop(field_name)
