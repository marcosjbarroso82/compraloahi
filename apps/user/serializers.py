from django.contrib.auth.models import User

from rest_framework import serializers

from apps.ad.models import Ad
from apps.userProfile.serializers import ProfileSerializer
from apps.msg.models import Msg
from apps.notification.models import Notification

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name','password',)


class UserAuthenticationSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)
    has_ads = serializers.SerializerMethodField(read_only=True)
    msg_unread = serializers.SerializerMethodField(read_only=True)
    notification_unread = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        depth = 2
        fields = ('profile', 'has_ads', 'msg_unread', 'notification_unread')

    def get_has_ads(self, obj):
        if Ad.objects.filter(author=obj.id).count() > 0:
            return True
        else:
            return False

    def get_msg_unread(self, obj):
        return Msg.objects.filter(recipient=obj.id, read_at=None).count()

    def get_notification_unread(self, obj):
        return Notification.objects.filter(receiver=obj.id, read=None).count()

    def get_profile(self, obj):
        return ProfileSerializer(instance=obj.profile).data