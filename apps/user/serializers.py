from django.contrib.auth.models import User

from rest_framework import serializers

from push_notifications.models import GCMDevice


class DeviceSerializer(serializers.ModelSerializer):
    device_id = serializers.StringRelatedField(allow_null=True)

    class Meta:
        model = GCMDevice
        fields = ('name', 'user', 'device_id', 'registration_id')
        read_only_fields = ('user', 'name')


    def create(self, validated_data):

        request = self.context.get('request', None)
        if request is not None:
           if request.user.is_authenticated():
                validated_data['name'] =  request.user.username
                validated_data['user'] = request.user

        return GCMDevice.objects.create(**validated_data)



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name','password',)



class UserByProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'username')
        read_only_fields = ('id')