from rest_framework import serializers
from .models import InterestGroup
from sorl.thumbnail import get_thumbnail
from apps.ad.serializers import Base64ImageField


class InterestGroupSerializer(serializers.ModelSerializer):
    thumbnail_250x160 = serializers.SerializerMethodField()
    image = Base64ImageField(max_length=None, use_url=True,)

    class Meta:
        model = InterestGroup
        read_only_fields = ('slug', 'owner')


    def get_thumbnail_250x160(self, obj):
        try:
            return get_thumbnail(obj.image, '250x160', crop='center', quality=99).url
        except:
            return ""

