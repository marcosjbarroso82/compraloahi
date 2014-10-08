from django.contrib.gis.db import models



class GeoLocation(models.Model):

    name = models.CharField(max_length=100)
    geometry = models.PointField()

    objects = models.GeoManager()

    def __str__(self):
        return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)