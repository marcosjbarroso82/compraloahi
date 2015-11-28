from django.utils.timezone import now as datetime_now
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

from taggit.managers import TaggableManager

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from apps.favorite.models import Favorite

import datetime


class AdQuerySet(models.QuerySet):

    def published(self):
        return self.filter(publish=True)


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

STATUS_AD = (
    ('1', 'Active'),
    ('0', 'Delete')
)

class Ad(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', unique_with='pub_date')
    published = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(User, related_name='ads')
    categories = models.ManyToManyField(Category)

    status = models.IntegerField(choices=STATUS_AD, default=1)

    short_description = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(default='0.00',
                                decimal_places=2,
                                max_digits=10)

    store_published = models.BooleanField(default=False)

    objects = AdQuerySet.as_manager()

    def show_location(self):
        return self.author.profile.privacy_settings.get('show_address')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ["-created"]

    def is_new(self):
        if (self.pub_date.date() + datetime.timedelta(days=30)) >= datetime.date.today():
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        self.created = datetime_now()
        self.published = True
        """
        if kwargs['pub_date'] < self.created:
            self.published = True
        else:
            self.published = False
        """
        instance = super(Ad, self).save(*args, **kwargs)
        for tag in self.title.split(' '):
            self.tags.add(tag)

        return instance

    def is_favorite(self, user):
        if Favorite.objects.get_favorite(user, self):
            return True
        else:
            return False


class AdImage(models.Model):
    ad_id = models.ForeignKey(Ad, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ad', null=False, blank=False, )
    default = models.BooleanField(default=False)


@receiver(pre_delete, sender=AdImage)
def adImage_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)
