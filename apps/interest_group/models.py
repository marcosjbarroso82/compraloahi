from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class InterestGroup(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(User)
    #TODO: Add upload_to and make sure thumbnails are still created
    image = models.ImageField(default='default.png', null=False, blank=False)
    slug = models.SlugField(auto_created=True, editable=False)

    def clean_slug(self):
        if self.name != '':
            #TODO: y esto? no parece estar bien!
            if InterestGroup.objects.get(slug= self.slug).count() > 0:
                raise ValidationError('Error, fields name is unique')

    def get_url(self):
        if self.slug:
            return reverse('group', args=[self.slug])
        else:
            return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)


    def __str__(self):
        return self.name