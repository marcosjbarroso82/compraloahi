from rest_framework import serializers
from postman.models import Message

class MessageSerializer(serializers.ModelSerializer):
    ad_id = serializers.IntegerField(allow_null=True, required=False)
    class Meta:
        model = Message
        read_only_fields = ('email', 'sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived', 'sender_deleted_at',
                            'recipient_deleted_at', 'moderation_by', )
        #extra_kwargs = {'ad_id': {'write_only': True}}
        write_only_fields = {'ad_id',}
        #fields = ('id', 'subject', 'ad_id')
