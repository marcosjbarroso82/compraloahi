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
    images = AdImageSerializer(many=True, read_only=True)
    class Meta:
        model = Ad
        #fields = ('title',)


class AdPublicSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    images = AdImageSerializer(many=True, read_only=True)

    class Meta:
        model= Ad
        fields = ('title', 'body', 'pub_date', 'categories', 'short_description', 'price', 'is_favorite', 'images')

    def get_is_favorite(self, obj):
        #request = self.context.get('request', None)
        #return obj.is_favorite(request.user)
        request = self.context.get('request', None)
        if request is not None:
           if request.user.is_authenticated():
               return obj.is_favorite(request.user)
           else:
               return False



class DistanceSerializer(serializers.Serializer):
    km = serializers.FloatField()
    m = serializers.FloatField()
    mi = serializers.FloatField()
    ft = serializers.FloatField()


class SearchResultSerializer(serializers.Serializer):

    title = serializers.CharField()
    pub_date = serializers.CharField()
    distance = serializers.SerializerMethodField('_distance')
    content_type = serializers.CharField(source='model_name')
    #content_object = serializers.SerializerMethodField('_content_object')
    content_object = serializers.SerializerMethodField('_content_object')

    def _content_object(self, obj):
        #assert False, obj.model_name
        if obj.model_name == 'ad':
            return AdSerializer(obj.object, many=False, context=self.context).data
            #return FoSerializer(obj.object, many=False, context=self.context).data
        if obj.model_name == 'Ad':
            return AdSerializer(obj.object, many=False, context=self.context).data
            #return BarSerializer(obj.object, many=False, context=self.context).data
        return {}

    def __init__(self,  *args, **kwargs):
        self.unit = kwargs.pop('unit', None)
        return super(SearchResultSerializer, self).__init__(*args, **kwargs)

    def _distance(self, obj):
        if self.unit:
            return {self.unit: getattr(obj.distance, self.unit)}
        try:
            return DistanceSerializer(obj.distance, many=False).data
        except Exception as e:
            ## Log this
            return {}