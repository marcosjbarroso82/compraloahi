

from django.db import models

from apps.ad.models import Ad
from django_pgjson.fields import JsonField
from django.core.exceptions import ValidationError

from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from apps.userProfile.models import UserProfile

INFO_ADDRESS = {
    "lat": '',
    "lng": '',
    "address": '',
    "nro": '',
    'country': '',
    'administrative_area_level_1': '',
    'administrative_area_level_2': '',
    'locality': ''
}
REQUIRED_INFO_ADDRESS = ['address', 'nro']

import random



class AdLocation(models.Model):
    title = models.CharField(max_length=40)
    ad = models.ForeignKey(Ad, related_name='locations', on_delete=models.CASCADE)#, unique=True)
    lat = models.FloatField()
    lng = models.FloatField()

    address = JsonField(default=INFO_ADDRESS)

    def clean(self):
        for key in REQUIRED_INFO_ADDRESS:
            if not key in self.address or not self.address[key]:
                raise ValidationError("The field %s to address is required" %(key))

        return super(AdLocation, self).clean()


    def save(self, loc, can_show, *args, **kwargs):
        self.address = self.address

        if not can_show: # TODO: Ofusca ubicacion
            min_random = 0.00000300
            max_random = 0.00000600
            if random.choice([True, False]):
                self.lat = float(loc.lat) + float(random.uniform(min_random, max_random)) #10 # TODO: Ofuscar ubicacion
            else:
                self.lat = float(loc.lat) - float(random.uniform(min_random, max_random))

            if random.choice([True, False]):
                self.lng = loc.lng + float(random.uniform(min_random, max_random))
            else:
                self.lng = loc.lng - float(random.uniform(min_random, max_random))
        else:
            self.lat = loc.lat
            self.lng = loc.lng
        super(AdLocation, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    def center(self):
        return {'latitude': self.lat, 'longitude': self.lng}