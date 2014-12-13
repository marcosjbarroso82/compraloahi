from rest_framework import serializers
from postman.models import Message

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        #fields = ('title',)
