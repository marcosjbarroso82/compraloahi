from rest_framework.serializers import ModelSerializer

from .models import UserProfile, Phone, UserLocation


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        depth = 2
        fields = ('image', 'birth_date', 'user')
        read_only_fields = ('user')

class PhoneSerializer(ModelSerializer):

    class Meta:
        model = Phone
        fields = ('number', 'type', 'userProfile')
        read_only_fields = ('userProfile')


class UserLocationSeralizer(ModelSerializer):

    class Meta:
        model = UserLocation
        fields = ('title', 'userProfile', 'lat', 'lng')
        read_only_fields = ('userProfile')
