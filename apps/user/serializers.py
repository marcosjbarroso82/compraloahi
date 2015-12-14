from django.contrib.auth.models import User

from rest_framework import serializers

from apps.ad.models import Ad
from apps.userProfile.serializers import ProfileSerializer, UserLocation
from apps.msg.models import Msg
from apps.notification.models import Notification

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name','password',)


class UserAuthenticationSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)
    has_items = serializers.SerializerMethodField(read_only=True)
    msg_unread = serializers.SerializerMethodField(read_only=True)
    notification_unread = serializers.SerializerMethodField(read_only=True)
    has_address = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        depth = 2
        fields = ('profile', 'has_items', 'msg_unread', 'notification_unread', 'has_address')

    def get_has_items(self, obj):
        if Ad.objects.filter(author=obj.id).count() > 0:
            return True
        else:
            return False

    def get_has_address(self, obj):
        if UserLocation.objects.filter(is_address=True, userProfile__user=obj.id).count():
            return True
        else:
            return False

    def get_msg_unread(self, obj):
        return Msg.objects.filter(recipient=obj.id, read_at=None).count()

    def get_notification_unread(self, obj):
        return Notification.objects.filter(receiver=obj.id, read=None, type='cmmt').count()

    def get_profile(self, obj):
        return ProfileSerializer(instance=obj.profile).data