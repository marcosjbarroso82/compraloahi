import ast
from rest_framework import serializers

from push_notifications.models import GCMDevice


from .models import Notification, ConfigNotification, TYPE_NOTIFICATION, CANAL_NOTIFICATION


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


class jsonFieldExtras(serializers.DictField):

    def get_attribute(self, instance):
        return instance.extras

    def to_representation(self, value):
        return ast.literal_eval(value)


class NotificationSerializer(serializers.ModelSerializer):
    extras = jsonFieldExtras()
    #extras = serializers.DictField()
    type = serializers.ChoiceField(choices=TYPE_NOTIFICATION)

    class Meta:
        model = Notification
        excluded = ('receiver')


class jsonField(serializers.DictField):

    def get_attribute(self, instance, *args, **kwargs):
        print(args)
        print(kwargs)
        return instance.config

    def to_representation(self, value):
        return value

class ConfigNotificationSerializer(serializers.ModelSerializer):
    configs = serializers.DictField(source='config')

    # def __init__(self, *args, **kwargs):
    #     super(ConfigNotificationSerializer, self).__init__(*args, **kwargs)
    #
    #     for type_key, type_value in TYPE_NOTIFICATION:
    #         for canal_key, canal_value in CANAL_NOTIFICATION:
    #             name = type_key + "_" + canal_key
    #             self.fields[name] = serializers.BooleanField(label=type_value + " " + canal_value)

    class Meta:
        model = ConfigNotification
        fields = ('configs', )

    # def to_representation(self, instance):
    #     obj = {}
    #     #obj['config'] = {}
    #     for type_key, type_value in TYPE_NOTIFICATION:
    #         for canal_key, canal_value in CANAL_NOTIFICATION:
    #             name = type_key + "_" + canal_key
    #             obj[name] = instance.has_perm(type_key, canal_key)
    #
    #     return obj
    #
    #
    # def to_internal_value(self, data):
    #     result = {}
    #     result['config'] = {}
    #     for type_key, type_value in TYPE_NOTIFICATION:
    #         result['config'][type_key] = {}
    #         for canal_key, canal_value in CANAL_NOTIFICATION:
    #             name = type_key + "_" + canal_key
    #             result['config'][type_key][canal_key] = bool(data.get(name, False)) #getattr(instance, name)
    #             result[name] = bool(data.get(name, False))
    #
    #     return result
    #
    # def update(self, instance, validated_data):
    #     instance.config = validated_data.get('config')
    #     instance.save()
    #
    #     return instance
