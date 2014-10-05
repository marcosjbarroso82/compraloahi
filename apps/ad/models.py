from django.db import models
from south.modelsinspector import add_introspection_rules
from .forms import StringListField

class TagField(models.TextField, metaclass=models.SubfieldBase):
    description = "Stores tags in a single database column."
    #__metaclass__ = models.SubfieldBase

    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)

    def __init__(self, delimiter=",", *args, **kwargs):
        self.delimiter = delimiter
        super(TagField, self).__init__(*args, **kwargs)


    def to_python(self, value):
        # If it's already a list, leave it
        if isinstance(value, list):
            #return value
            return value
        if value is None:
            return []
        if value == "":
            return []
        # Otherwise, split by delimiter
        return value.split(self.delimiter)

    def get_prep_value(self, value):
        if isinstance(value, list):
            return ",".join(value)
        return ""
"""
add_introspection_rules([
    (
        [TagField], # Class(es) these apply to
        [],         # Positional arguments (not used)
        {           # Keyword argument
            "delimiter": ["delimiter", {"default": ","}],
        },
    ),
], ["^ad\.models\.TagField"])
"""


class AdQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)



class Ad(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default=True)
    tags_temp6 = TagField()
    # tags []
    # price (moneda)
    # author. foreingkey.

    objects = AdQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ["-created"]

class AdImage(models.Model):
    ad_id = models.ForeignKey(Ad, related_name='images')
    image = models.ImageField(upload_to='ad')