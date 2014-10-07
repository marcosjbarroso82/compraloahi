from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from apps.agenda.models import Agenda
#from apps import agenda.models.


class AdQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Ad(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager()
    author = models.ForeignKey(User, related_name='ads')
    #agenda = models.OneToOneField(Agenda, null=True, on_delete=models.CASCADE)
    #agenda = models.ForeignKey(Agenda, unique=True, null=True, on_delete=SET_NULL)
    agenda = models.ForeignKey(Agenda, unique=True, null=True, on_delete=models.SET_NULL, blank=True)
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

    def delete(self, *args, **kwargs):
        if self.agenda != None:
            self.agenda.delete()
        return super(self.__class__, self).delete(*args, **kwargs)
    """
    def pre_delete_handler(self):
        self.agenda.delete()
        pass
    """

class AdImage(models.Model):
    ad_id = models.ForeignKey(Ad, related_name='images')
    image = models.ImageField(upload_to='ad')