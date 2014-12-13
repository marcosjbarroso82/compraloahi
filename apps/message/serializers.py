from rest_framework import serializers
from postman.models import Message
import json
from django.core import serializers as core_serializers
"""
class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        depth = 1
        #fields = ('title',)
"""


class MessageListSerializer(serializers.ListSerializer):
    class Meta:
        model = Message
        fields = ("id")

    def update(self, instance, validated_data):
        ret = []
        return ret



class MessageSerializer(serializers.Serializer):

    class Meta:
        list_serializer_class = MessageListSerializer

    def to_representation(self, obj):
        return {
            'pk': obj.pk,
            'body': obj.body,
            'sent_at': obj.sent_at,
            'sender_archived ': obj.sender_archived,
            'recipient_archived': obj.recipient_archived,
            'sender_deleted_at': obj.recipient_archived,
            'recipient_deleted_at': obj.recipient_archived,
            'read_at': obj.recipient_archived,
            'subject': obj.subject
        }


