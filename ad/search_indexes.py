import datetime
from haystack import indexes
from .models import Ad
from django.contrib.auth.models import User


class AdIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/ad/ad_text.txt')

    #model fields
    title = indexes.CharField(model_attr='title')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    #tags = indexes.CharField()
    #tags = indexes.CharField(faceted=True, )
    #author = indexes.CharField()
    #author = indexes.CharField(model_attr='author')
    author = indexes.CharField(model_attr='author', faceted=True)

    def prepare(self, object):
        self.prepared_data = super(AdIndex, self).prepare(object)

        # Add in tags (assuming there's a M2M relationship to Tag on the model).
        # Note that this would NOT get picked up by the automatic
        # schema tools provided by Haystack.
        self.prepared_data['tags'] = [tag.name for tag in object.tags.all()]

        return self.prepared_data

    """
    def prepare_tags(self, obj):
        return [tag.name for tag in Ad.tags.all()]
    """

    class Meta:
        model = Ad

    def get_model(self):
        return Ad

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

