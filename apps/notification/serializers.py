import ast
from rest_framework import serializers

from push_notifications.models import GCMDevice


from .models import Notification, ConfigNotification, TYPE_NOTIFICATION


class DeviceSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(allow_null=True, required=False, max_length=255)

    class Meta:
        model = GCMDevice
        fields = ('name', 'user', 'device_id', 'registration_id')
        read_only_fields = ('user', 'name')

    def create(self, validated_data):
        # TODO: Validad campos
        request = self.context.get('request', None)
        if request is not None:
            if request.user.is_authenticated():
                validated_data['name'] =  request.user.username
                validated_data['user'] = request.user
        return GCMDevice.objects.create(**validated_data)


class NotificationSerializer(serializers.ModelSerializer):
    extras = serializers.DictField()
    type = serializers.ChoiceField(choices=TYPE_NOTIFICATION)

    class Meta:
        model = Notification
        excluded = ('receiver')


class ConfigNotificationSerializer(serializers.ModelSerializer):
    configs = serializers.DictField(source='config')

    class Meta:
        model = ConfigNotification
        fields = ('configs', )

