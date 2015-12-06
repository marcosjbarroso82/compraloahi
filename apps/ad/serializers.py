from rest_framework import serializers
from .models import Ad, AdImage, Category
from sorl.thumbnail import get_thumbnail
from apps.adLocation.models import AdLocation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True,)
    thumbnail_110x110 = serializers.SerializerMethodField()
    # TODO: Validar que los avisos solo sean del mismo autor

    def __init__(self, *args, **kwargs):
        super(ImageSerializer, self).__init__(*args, **kwargs)
        action = self.context['view'].action
        if not action == 'create' and not action == 'update':
            self.fields['image'].read_only = True

        if action != 'create':
            self.fields['ad'].read_only = True

    def get_thumbnail_110x110(self, obj):
        try:
            return get_thumbnail(obj.image, '110x110', crop='center', quality=99).url
        except:
            return ""

    class Meta:
        model = AdImage
        fields = ('image', 'id', 'ad', 'default', 'thumbnail_110x110')
        read_only_fields = ('id',)


class AdImageSerializer(serializers.ModelSerializer):
    thumbnail_110x110 = serializers.SerializerMethodField()
    thumbnail_800x800 = serializers.SerializerMethodField()

    class Meta:
        model = AdImage
        #fields = ('title',)
        #exclude = ('ad' , )

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
        fields = ('id', 'images', 'title', 'body', 'status', 'pub_date', 'price', 'slug', 'short_description',
                  'author', 'categories', 'locations', 'is_favorite', 'status')
        #exclude = ('author', 'created', 'modified',)
        read_only_fields = ('pub_date', 'id', 'pub_date', 'slug', 'tags', 'author', 'status')

    def get_is_favorite(self, obj):
        request = self.context.get('request', None)
        return obj.is_favorite(request.user)


    def __init__(self, *args, **kwargs):
        super(AdSerializer, self).__init__(*args, **kwargs)
        action = self.context['view'].action

        if action == 'create':
            self.fields.pop('status')


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
        return AdImageSerializer(AdImage.objects.filter(ad=obj.object), many=True).data

    def get_image(self, obj):
        return AdImageSerializer(AdImage.objects.filter(ad=obj.object).first()).data['thumbnail_110x110']

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

