from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import UserProfile, Phone, UserLocation, Store, REQUIRED_INFO_ADDRESS, CONFIG_PRIVACY

from sorl.thumbnail import get_thumbnail

from django.contrib.auth.models import User


class StoreSerializer(ModelSerializer):
    logo = serializers.SerializerMethodField()
    style = serializers.DictField()

    class Meta:
        model = Store
        fields = ('name', 'style', 'logo', 'slug', 'slogan')
        read_only_fields = ('slug',)

    def get_logo(self, obj):
        if obj.logo:
            return obj.logo.url
        else:
            return ""


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = ('number', 'type', 'id')


class UserProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'username')
        read_only_fields = ('id')

    def create(self, validated_data):
        if validated_data.get('username'):
            if User.objects.filter(username=validated_data.get('username')).count() > 0:
                raise serializers.ValidationError("create - El username ya existe")
        else:
            raise serializers.ValidationError("create - username es requerido ")
        return super(UserProfileSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        # Check no other user has the same name
        if validated_data.get('username'):
            if User.objects.filter(username=validated_data.get('username') ).exclude(pk=instance.id).count() > 0:
                raise serializers.ValidationError("username must be unique")
        else:
            raise serializers.ValidationError(" username eis required")
        return super(UserProfileSerializer, self).update(instance, validated_data)


class ProfileLocationSerializer(ModelSerializer):
    """
        Serializer to Userlocation for profile.
    """
    address = serializers.DictField()

    class Meta:
        model = UserLocation
        fields = ('title', 'lat', 'lng', 'address', 'id')
        read_only_fields = ('id', )
        excluded = ('userProfile', 'is_address', 'radius')
        depth = 1

    def validate(self, attrs):
        for key in REQUIRED_INFO_ADDRESS:
            if not key in attrs['address'] or not attrs['address'][key]:
                raise serializers.ValidationError("The param - %s - to address is required" %(key))

        return super(ProfileLocationSerializer, self).validate(attrs)

    def __init__(self, *args, **kwargs):
        super(ProfileLocationSerializer, self).__init__(*args, **kwargs)
        if not self.instance:
            request = self.context.get('request', None)
            self.instance = UserLocation()
            self.instance.userProfile = request.user.profile
            self.instance.radius = 5000
            self.instance.is_address = True


    def create(self, validated_data):
        request = self.context.get('request', None)
        if request is not None:
            if request.user.is_authenticated():
                validated_data['userProfile'] =  request.user.profile
                validated_data['radius'] = 5000
                validated_data['is_address'] = True
        return UserLocation.objects.create(**validated_data)



class ConfigPrivacitySerializer(ModelSerializer):
    config = serializers.DictField(source='privacy_settings')

    def validate(self, attrs):
        for key, value in CONFIG_PRIVACY.items():
            if not key in attrs['privacy_settings'] or not type(attrs['privacy_settings'][key]) is bool:
                raise serializers.ValidationError("The param %s to config privacity is required" %(key))

        return super(ConfigPrivacitySerializer, self).validate(attrs)

    class Meta:
        model = UserProfile
        fields = ('config',)
        depth = 1


class ProfileSerializer(ModelSerializer):
    thumbnail_200x200 = serializers.SerializerMethodField()
    phones = PhoneSerializer(many=True)
    user = UserProfileSerializer()
    image = serializers.ImageField(allow_empty_file=True, use_url=True, read_only=True)

    class Meta:
        model = UserProfile
        depth = 2
        fields = ('image', 'birth_date', 'user', 'phones', 'thumbnail_200x200', 'id')
        read_only_fields = ('id',)


    def update(self, instance, validated_data):
        user_data = validated_data.get('user', instance.user)
        request = self.context.get('request', None)
        user_serializer = UserProfileSerializer()
        instance.user = user_serializer.update(instance=request.user, validated_data=user_data)

        phones_data = validated_data.get('phones', [])
        if phones_data:
            Phone.objects.filter(userProfile=instance).delete()
            for phone in phones_data:
                p = Phone()
                p.userProfile = instance
                p.number= int(phone.get('number', 0))
                p.type = phone.get('type', 'TEL')
                p.save()

        instance.birth_date = validated_data.get('birth_date', instance.birth_date)

        instance.save()

        return instance

    def get_thumbnail_200x200(self, obj):
        return get_thumbnail(obj.image, '400x400', crop='center', quality=99).url


class UserLocationSeralizer(ModelSerializer):
    center = serializers.SerializerMethodField()

    class Meta:
        model = UserLocation
        fields = ('title', 'lat', 'lng', 'center', 'radius', 'id')
        excluded = ('userProfile',)
        depth = 1

    def get_center(self, obj):
        center = {'latitude': obj.lat, 'longitude': obj.lng}
        return center

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request is not None:
            if request.user.is_authenticated():
                validated_data['userProfile'] =  request.user.profile
        return UserLocation.objects.create(**validated_data)


