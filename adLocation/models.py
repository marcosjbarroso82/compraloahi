from django.db import models
from ad.models import Ad


class AdLocation(models.Model):
    title = models.CharField(max_length=40)
    ad = models.ForeignKey(Ad, related_name='locations', unique=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.title
