from rest_framework import serializers
from .models import InterestGroup, Post, MemberShipRequest, Membership
from sorl.thumbnail import get_thumbnail
from apps.ad.serializers import Base64ImageField


class MemberShipSerializer(serializers.ModelSerializer):
    member = serializers.SerializerMethodField()

    class Meta:
        model = Membership

    def get_member(self, obj):
        return {
            'name': obj.user.username,
            'image': get_thumbnail(obj.user.profile.image, '110x110', crop='center', quality=99).url
        }

class MemberShipRequestSerializer(serializers.ModelSerializer):
    member = serializers.SerializerMethodField()
    display_status = serializers.SerializerMethodField()

    class Meta:
        model = MemberShipRequest
        exclude = ('hash_validation', 'status', 'user', 'updated')

    def get_member(self, obj):
        if obj.user:
            return {
                'name': obj.user.username,
                'image': get_thumbnail(obj.user.profile.image, '110x110', crop='center', quality=99).url
            }

    def get_display_status(self, obj):
        return obj.get_status_display()


class InterestGroupSerializer(serializers.ModelSerializer):
    thumbnail_250x160 = serializers.SerializerMethodField()
    image = Base64ImageField(max_length=None, use_url=True, required=False)
    image_header = Base64ImageField(max_length=None, use_url=True, required=False)
    #members = serializers.SerializerMethodField()

    class Meta:
        model = InterestGroup
        read_only_fields = ('slug', 'owner')

    # def __init__(self, *args, **kwargs):
    #     super(InterestGroupSerializer, self).__init__(*args, **kwargs)
    #
    #     action = self.context['view'].action
    #     not_allowed_to_show = ()
    #     if action != 'members':
    #         not_allowed_to_show = ('members',)
    #
    #     for field_name in not_allowed_to_show:
    #         self.fields.pop(field_name)

    # def get_members(self, obj):
    #     members = []
    #     request = self.context.get('request', None)
    #     for member in obj.members.exclude(pk=request.user.profile.id):
    #         members.append({'id': member.pk,
    #                         'email': member.user.email,
    #                         'image': get_thumbnail(member.image, '110x110', crop='center', quality=99).url})
    #
    #     return members

    def get_thumbnail_250x160(self, obj):
        try:
            return get_thumbnail(obj.image, '250x160', crop='center', quality=99).url
        except Exception as e:
            return ""


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('content', 'group', 'created', 'id', 'user')
        read_only_fields = ('created', 'id', 'user')

    def get_user(self, obj):
        if obj.user:
            return {
                'username': obj.user.username,
                'image': get_thumbnail(obj.user.profile.image, '110x110', crop='center', quality=99).url
            }