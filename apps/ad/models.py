from django.utils.timezone import now as datetime_now
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

from taggit.managers import TaggableManager

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.contenttypes.fields import GenericRelation

from favit.models import Favorite


class AdQuerySet(models.QuerySet):

    def published(self):
        return self.filter(publish=True)


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique_with='pub_date')
    published = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(User, related_name='ads')
    categories = models.ManyToManyField(Category)

    short_description = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(default='0.00',
                                decimal_places=2,
                                max_digits=10)

    # Instance of manager to Favorite Objects
    #favorites = GenericRelation(Favorite,
    #                            content_type_field='target_content_type',
    #                            object_id_field='target_object_id')

    objects = AdQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        self.created = datetime_now()
        self.published = True
        """
        if kwargs['pub_date'] < self.created:
            self.published = True
        else:
            self.published = False
        """
        super(Ad, self).save(*args, **kwargs)


    def is_favorite(self, user):
        if Favorite.objects.get_favorite(user, self):
            return True
        else:
            return False


class AdImage(models.Model):
    ad_id = models.ForeignKey(Ad, related_name='images')
    image = models.ImageField(upload_to='ad', null=False, blank=False, )


@receiver(pre_delete, sender=AdImage)
def adImage_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)
