from rest_framework import serializers
from .models import Ad, AdImage
from sorl.thumbnail import get_thumbnail


class AdImageSerializer(serializers.ModelSerializer):
    thumbnail_90x90 = serializers.SerializerMethodField()

    class Meta:
        model = AdImage
        #fields = ('title',)

    def get_thumbnail_90x90(self, obj):
        return get_thumbnail(obj.image, '90x90', crop='center', quality=99).url


class AdSerializer(serializers.ModelSerializer):
    #images = serializers.
    images = AdImageSerializer(many=True, read_only=True)
    class Meta:
        model = Ad
        #fields = ('title',)
