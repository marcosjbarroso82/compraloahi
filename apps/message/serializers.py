from rest_framework import serializers
from postman.models import Message

"""
class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        depth = 1
        #fields = ('title',)
"""


class MessageListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        messages = [Message(**item) for item in validated_data]
        return Message.objects.bulk_create(messages)

    class Meta:
        model = Message

class MessageSerializer(serializers.Serializer):

    class Meta:
        list_serializer_class = MessageListSerializer
        model = Message
