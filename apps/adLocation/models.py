import urllib.request
import json

from django.db import models

from apps.ad.models import Ad


class AdLocation(models.Model):
    title = models.CharField(max_length=40)
    ad = models.ForeignKey(Ad, related_name='locations', unique=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    country = models.CharField(max_length=40, blank=True, null=True)
    administrative_area_level_1 = models.CharField(max_length=40, blank=True, null=True)
    administrative_area_level_2 = models.CharField(max_length=40, blank=True, null=True)
    locality = models.CharField(max_length=40, blank=True, null=True)

    def save(self, *args, **kwargs):
        url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng='+ str(self.lat) + ',' + str(self.lng) +'&sensor=true'
        print(url)
        response = urllib.request.urlopen(url)
        print(response)
        json_response = response.read()

        obj = json.loads(json_response.decode("utf-8"))

        for district in obj["results"][0]["address_components"]:
            if "locality" in district["types"]:
                self.locality = district["long_name"]
            elif "administrative_area_level_2" in district["types"]:
                self.administrative_area_level_2 = district["long_name"]
            elif "administrative_area_level_1" in district["types"]:
                self.administrative_area_level_1 = district["long_name"]
            elif "country" in district["types"]:
                self.country = district["long_name"]

        super(AdLocation, self).save(*args, **kwargs) # Call the "real" save() method.

    def __str__(self):
        return self.title