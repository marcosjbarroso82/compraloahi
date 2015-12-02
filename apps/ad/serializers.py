from rest_framework import serializers
from .models import Ad, AdImage, Category
from sorl.thumbnail import get_thumbnail
from apps.adLocation.models import AdLocation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

class AdImageSerializer(serializers.ModelSerializer):
    thumbnail_110x110 = serializers.SerializerMethodField()
    thumbnail_800x800 = serializers.SerializerMethodField()

    class Meta:
        model = AdImage
        #fields = ('title',)
        exclude = ('ad_id' , )

    def get_thumbnail_110x110(self, obj):
        try:
            return get_thumbnail(obj.image, '110x110', crop='center', quality=99).url
        except:
            return ""

    def get_thumbnail_800x800(self, obj):
        try:
            return get_thumbnail(obj.image, '800x800', crop='center', quality=99).url
        except:
            return ""


class AdLocationSerializer(serializers.ModelSerializer):
    #center = serializers.SerializerMethodField()

    class Meta:
        model = AdLocation
        fields = ('title', 'lat', 'lng', 'id', 'ad', 'address')

    def __init__(self, *args, **kwargs):
        super(AdLocationSerializer, self).__init__(*args, **kwargs)

        if not self.instance or not self.instance.ad.show_location():
            self.fields.pop('address')


    # def get_center(self, obj):
    #     return obj.center()


class AdSerializer(serializers.ModelSerializer):
    images = AdImageSerializer(many=True, read_only=True)
    is_favorite = serializers.SerializerMethodField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10, coerce_to_string=False)
    locations = AdLocationSerializer(many=True, read_only=True)
    # TODO: Falta validar que si o si halla una categoria

    class Meta:
        model = Ad

    def get_is_favorite(self, obj):
        request = self.context.get('request', None)
        return obj.is_favorite(request.user)


class AdPublicSerializer(serializers.ModelSerializer):
    images = AdImageSerializer(many=True, read_only=True)
    is_favorite = serializers.SerializerMethodField()
    locations = AdLocationSerializer(many=True, read_only=True)

    class Meta:
        model= Ad
        fields = ('id','title', 'body', 'pub_date', 'categories', 'short_description', 'price', 'is_favorite', 'images', 'locations')

    def get_is_favorite(self, obj):
        request = self.context.get('request', None)
        if request is not None:
           if request.user.is_authenticated():
               return obj.is_favorite(request.user)
           else:
               return False
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
    images = serializers.SerializerMethodField()
    center = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_center(self, obj):
        location = AdLocation.objects.filter(ad=obj.object).first()
        center = {}
        center['lat'] = location.lat
        center['lng'] = location.lng
        return center

    def get_images(self, obj):
        return AdImageSerializer(AdImage.objects.filter(ad_id=obj.object), many=True).data

    def get_image(self, obj):
        return AdImageSerializer(AdImage.objects.filter(ad_id=obj.object).first()).data['thumbnail_110x110']

    def get_is_favorite(self, obj):
        request = self.context.get('request', None)
        if request is not None:
           if request.user.is_authenticated():
               return obj.object.is_favorite(request.user)
           else:
               return False
        else:
            return False

class SearchResultSerializer(serializers.Serializer):
    facets = serializers.ListField()
    count = serializers.IntegerField()
    paginated_by = serializers.IntegerField()
    page = serializers.IntegerField()
    next = serializers.IntegerField()
    previous = serializers.IntegerField()
    #results = AdsSearchSerializer(many=True, source='object_list')

    def __init__(self, *args, **kwargs):
        super(SearchResultSerializer, self).__init__(*args, **kwargs)
        self.fields['results'] = AdsSearchSerializer(many=True, source='object_list', context=self.context)

