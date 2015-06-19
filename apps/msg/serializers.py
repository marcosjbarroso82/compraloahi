from . import models
from rest_framework import serializers

class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Msg

        read_only_fields = ('sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived', 'sender_deleted_at',
                            'recipient_deleted_at', 'sender', 'moderation_status',
                            'parent', 'thread', 'moderation_reason', 'moderation_date')

class MsgSerializer2(serializers.ModelSerializer):
    class Meta:
        model = models.Msg
        fields = ('pk',)

        read_only_fields = ('subject', 'body', 'sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived', 'sender_deleted_at',
                            'recipient_deleted_at', 'sender', 'moderation_status',
                            'parent', 'thread', 'moderation_reason', 'moderation_date')