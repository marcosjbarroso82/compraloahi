from rest_framework import serializers
from .models import Ad, AdImage
from sorl.thumbnail import get_thumbnail
from apps.adLocation.models import AdLocation


class AdImageSerializer(serializers.ModelSerializer):
    thumbnail_90x90 = serializers.SerializerMethodField()

    class Meta:
        model = AdImage
        #fields = ('title',)
        exclude = ('id', 'ad_id')

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
        fields = ('id','title', 'body', 'pub_date', 'categories', 'short_description', 'price', 'is_favorite', 'images')

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



class AdsSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='pk')
    title = serializers.CharField()
    pub_date = serializers.DateTimeField()
    price = serializers.FloatField()
    short_description = serializers.CharField()
    slug = serializers.CharField()
    is_favorite = serializers.SerializerMethodField()
    #thumbnail_90x90 = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    center = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_center(self, obj):
        location = AdLocation.objects.filter(ad=obj.object).first()
        center = {}
        center['latitude'] = location.lat
        center['longitude'] = location.lng
        return center

    def get_images(self, obj):
        return AdImageSerializer(AdImage.objects.filter(ad_id=obj.object), many=True).data
        #return get_thumbnail(AdImage.objects.filter(ad_id=obj.object).first(), '90x90', crop='center', quality=99).url

    def get_image(self, obj):
        return AdImageSerializer(AdImage.objects.filter(ad_id=obj.object).first()).data['thumbnail_90x90']

    # def get_thumbnail_90x90(self, obj):
    #     thumbs = []
    #     for image in AdImage.objects.filter(ad_id=obj.object):
    #         thumbs.append(get_thumbnail(image, '90x90', crop='center', quality=99).url)
    #
    #     return thumbs


    def get_is_favorite(self, obj):
        request = self.context.get('request', None)
        if request is not None:
           if request.user.is_authenticated():
               return obj.object.is_favorite(request.user)
           else:
               return False

class SearchResultSerializer(serializers.Serializer):
    facets = serializers.ListField()
    count = serializers.IntegerField()
    next = serializers.IntegerField()
    previous = serializers.IntegerField()
    results = AdsSearchSerializer(many=True, source='object_list')

    #def get_results(self, obj):
    #    return AdsSearchSerializer(obj.object_list, many=True).data

    # def get_next(self, obj):
    #     return 10
    #     #if self.obj.has_next():
    #     #    return self.obj.next_page_number()
    #     #else:
    #     #    return None
    #
    # def get_previous(self, obj):
    #     return 5
    #     # if self.obj.has_previous():
    #     #     return self.obj.previous_page_number()
    #     # else:
    #     #     return None
    #
    # def get_count(self, obj):
    #     return 1
        #return self.obj.count


    #content_type = serializers.CharField(source='model_name')
    #content_object = serializers.SerializerMethodField('_content_object')
    #distance = serializers.SerializerMethodField('_distance')






    # def _content_object(self, obj):
    #     #assert False, obj.model_name
    #     if obj.model_name == 'ad':
    #         return AdPublicSerializer(obj.object, many=False, context=self.context).data
    #         #return FoSerializer(obj.object, many=False, context=self.context).data
    #     if obj.model_name == 'Ad':
    #         return AdPublicSerializer(obj.object, many=False, context=self.context).data
    #         #return BarSerializer(obj.object, many=False, context=self.context).data
    #     return {}

    #def __init__(self,  *args, **kwargs):
    #    self.unit = kwargs.pop('unit', None)
    #    return super(SearchResultSerializer, self).__init__(*args, **kwargs)

    #def _distance(self, obj):
    #    if self.unit:
    #        return {self.unit: getattr(obj.distance, self.unit)}
    #    try:
    #        return DistanceSerializer(obj.distance, many=False).data
    #    except Exception as e:
    #        ## Log this
    #        return {}
