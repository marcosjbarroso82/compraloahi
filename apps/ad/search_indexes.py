import datetime

from haystack import indexes

from .models import Ad


class AdIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/ad/ad_text.txt')

    #model fields
    title = indexes.CharField(model_attr='title')
    short_description = indexes.CharField(model_attr='short_description')
    slug = indexes.CharField(model_attr='slug')
    price = indexes.FloatField(model_attr='price')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    tags = indexes.CharField()
    image1 = indexes.CharField()
    localities = indexes.CharField(faceted=True)
    provinces = indexes.CharField(faceted=True)
    administrative_area_level_2 = indexes.CharField(faceted=True)
    categories = indexes.MultiValueField(faceted=True)

    location = indexes.LocationField()

    def prepare_location(self, obj):
        # If you're just storing the floats...
        return "%s,%s" % (obj.locations.first().lat, obj.locations.first().lng)

    def prepare_image1(self, obj):
        return str(obj.images.first().image)

    def prepare(self, object):
        self.prepared_data = super(AdIndex, self).prepare(object)

        self.prepared_data['tags'] = [tag.name for tag in object.tags.all()]
        self.prepared_data['categories'] = [category.name for category in object.categories.all()]
        self.prepared_data['localities'] = [location.locality for location in object.locations.all()]
        self.prepared_data['provinces'] = [location.administrative_area_level_1 for location in object.locations.all()]
        self.prepared_data['administrative_area_level_2'] = [location.administrative_area_level_2 for location in object.locations.all()]

        return self.prepared_data

    class Meta:
        model = Ad

    def get_model(self):
        return Ad

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

