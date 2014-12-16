from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import UserProfile, Phone, UserLocation

from sorl.thumbnail import get_thumbnail


class PhoneSerializer(ModelSerializer):

    class Meta:
        model = Phone
        fields = ('number', 'type')


class UserProfileSerializer(ModelSerializer):
    thumbnail_200x200 = serializers.SerializerMethodField()
    phones = PhoneSerializer(many=True)

    class Meta:
        model = UserProfile
        depth = 2
        fields = ('image', 'birth_date', 'user', 'phones', 'thumbnail_200x200')
        read_only_fields = ('user')

    def get_thumbnail_200x200(self, obj):
        return get_thumbnail(obj.image, '200x200', crop='center', quality=99).url


class UserLocationSeralizer(ModelSerializer):

    class Meta:
        model = UserLocation
        #fields = ('title', 'userProfile', 'lat', 'lng')
        read_only_fields = ('userProfile')

    center = serializers.SerializerMethodField()
    radius = serializers.SerializerMethodField()


    def get_center(self, obj):
        center = {'latitude': obj.lat, 'longitude': obj.lng}
        return center

    def get_radius(self, obj):
        return 5000
