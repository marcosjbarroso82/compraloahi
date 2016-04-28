from rest_framework import serializers
from .models import InterestGroup
from sorl.thumbnail import get_thumbnail


class InterestGroupSerializer(serializers.ModelSerializer):
    thumbnail_250x160 = serializers.SerializerMethodField()

    class Meta:
        model = InterestGroup

    def get_thumbnail_250x160(self, obj):
        try:
            return get_thumbnail(obj.image, '250x160', crop='center', quality=99).url
        except:
            return ""

