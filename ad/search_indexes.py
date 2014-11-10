import datetime
from haystack import indexes
from .models import Ad
from django.contrib.auth.models import User


class AdIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/ad/ad_text.txt')

    #model fields
    title = indexes.CharField(model_attr='title')
    price = indexes.FloatField(model_attr='price')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    tags = indexes.CharField()
    localities = indexes.CharField(faceted=True)
    administrative_area_level_1 = indexes.CharField(faceted=True)
    administrative_area_level_2 = indexes.CharField(faceted=True)
    categories = indexes.MultiValueField(faceted=True)

    def prepare(self, object):
        self.prepared_data = super(AdIndex, self).prepare(object)

        self.prepared_data['tags'] = [tag.name for tag in object.tags.all()]
        self.prepared_data['categories'] = [category.name for category in object.categories.all()]
        self.prepared_data['localities'] = [location.locality for location in object.locations.all()]
        self.prepared_data['administrative_area_level_1'] = [location.administrative_area_level_1 for location in object.locations.all()]
        self.prepared_data['administrative_area_level_2'] = [location.administrative_area_level_2 for location in object.locations.all()]

        return self.prepared_data

    class Meta:
        model = Ad

    def get_model(self):
        return Ad

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

