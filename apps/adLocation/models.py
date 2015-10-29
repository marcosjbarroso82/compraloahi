

from django.db import models

from apps.ad.models import Ad
from django_pgjson.fields import JsonField
from django.core.exceptions import ValidationError


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
REQUIRED_INFO_ADDRESS = ['lat', 'lng', 'address', 'nro']


class AdLocation(models.Model):
    title = models.CharField(max_length=40)
    ad = models.ForeignKey(Ad, related_name='locations', on_delete='cascade')#, unique=True)
    lat = models.FloatField()
    lng = models.FloatField()

    address = JsonField(default=INFO_ADDRESS)

    def clean(self):
        for key in REQUIRED_INFO_ADDRESS:
            if not key in self.address or not self.address[key]:
                raise ValidationError("The field %s to address is required" %(key))

        return super(AdLocation, self).clean()


    def save(self, *args, **kwargs):

        if self.ad.show_location():
            self.lat = self.address.get('lat')
            self.lng = self.address.get('lng')
        else:
            self.lat = self.address.get('lat') + 10 # TODO: Ofuscar ubicacion
            self.lng = self.address.get('lng') + 10
        super(AdLocation, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    def center(self):
        return {'latitude': self.lat, 'longitude': self.lng}