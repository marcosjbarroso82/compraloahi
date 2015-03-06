from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import UserProfile, Phone, UserLocation

from sorl.thumbnail import get_thumbnail

from apps.user.serializers import UserByProfileSerializer



class PhoneSerializer(ModelSerializer):

    class Meta:
        model = Phone
        fields = ('number', 'type', 'id')


class UserProfileSerializer(ModelSerializer):
    thumbnail_200x200 = serializers.SerializerMethodField()
    phones = PhoneSerializer(many=True)
    user = UserByProfileSerializer()
    image = serializers.ImageField(allow_empty_file=True, use_url=True)

    class Meta:
        model = UserProfile
        depth = 2
        fields = ('image', 'birth_date', 'user', 'phones', 'thumbnail_200x200', 'id')
        read_only_fields = ('user', 'id')
        #write_only_fields = ('image',)

    def get_thumbnail_200x200(self, obj):
        return get_thumbnail(obj.image, '400x400', crop='center', quality=99).url


class UserLocationSeralizer(ModelSerializer):

    class Meta:
        model = UserLocation
        #fields = ('title', 'userProfile', 'lat', 'lng')
        read_only_fields = ('userProfile')
        depth = 1

    center = serializers.SerializerMethodField()


    def get_center(self, obj):
        center = {'latitude': obj.lat, 'longitude': obj.lng}
        return center


