from django.utils.timezone import now as datetime_now
from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


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
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(User, related_name='ads')

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


class AdImage(models.Model):
    ad_id = models.ForeignKey(Ad, related_name='images')
    image = models.ImageField(upload_to='ad')
