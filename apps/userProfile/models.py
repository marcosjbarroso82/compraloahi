from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django_pgjson.fields import JsonField
from django.core.urlresolvers import reverse
import urllib.request
import json

TYPE_PHONE = (
    ('TEL', 'Telefono'),
    ('CEL', 'Celular'),
    ('FAX', 'Fax'),
)

CONFIG_PRIVACY = {
    'show_address': True,
}

class UserProfile(models.Model):
    image = models.ImageField(upload_to='profile', null=False, blank=False, default="profile/default.jpg")
    birth_date = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, unique=True, related_name='profile')

    privacy_settings = JsonField(default=CONFIG_PRIVACY)

    def __str__(self):
        return 'profile ' + self.user.username

    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        self.privacy_settings_old = self.privacy_settings


    def change_privacity(self):
        if self.privacy_settings.get('show_address', True) == self.privacy_settings_old.get('show_address', True):
            return False
        else:
            return True

    def get_can_show_location(self):
        return self.privacy_settings.get('show_address', True)

    def save(self, *args, **kwargs):
        obj = super(UserProfile, self).save(*args, **kwargs)
        if self.change_privacity():
            self.locations.filter(is_address=True).first().save()

        return obj
    # def clean(self):
    #     # Validate if has all config
    #     for key, value in CONFIG_PRIVACY.items():
    #         if not key in self.privacy_settings or not type(self.privacy_settings[key]) is bool:
    #             raise ValidationError("The param %s to config privacity is required" %(key))
    #
    #     return super(UserProfile, self).clean()


class Phone(models.Model):
    number = models.BigIntegerField()
    type = models.CharField(max_length=200, choices=TYPE_PHONE)
    userProfile = models.ForeignKey(UserProfile, related_name='phones')



INFO_ADDRESS = {
    "address": '',
    "nro": '',
    'country': '',
    'administrative_area_level_1': '',
    'administrative_area_level_2': '',
    'locality': ''
}
REQUIRED_INFO_ADDRESS = ['address', 'nro']


class UserLocation(models.Model):
    title = models.CharField(max_length=100)
    userProfile = models.ForeignKey(UserProfile, related_name='locations')
    lat = models.FloatField(null=False)
    lng = models.FloatField(null=False)
    radius = models.IntegerField(default=5000)
    is_address = models.BooleanField(default=False)

    address = JsonField(default=INFO_ADDRESS)

    def get_address(self):
        address = self.address
        address['lat'] = self.lat
        address['lng'] = self.lng
        return address

    def save(self, *args, **kwargs):
        try:
            url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng='+ \
                  str(self.lat) + ',' + str(self.lng) +'&sensor=true'

            response = urllib.request.urlopen(url)
            json_response = response.read()
            obj = json.loads(json_response.decode("utf-8"))
            if len(obj['results']):
                for district in obj["results"][0]["address_components"]:
                    if "locality" in district["types"]:
                        self.address['locality'] = district["long_name"]
                    elif "administrative_area_level_2" in district["types"]:
                        self.address['administrative_area_level_2'] = district["long_name"]
                    elif "administrative_area_level_1" in district["types"]:
                        self.address['administrative_area_level_1'] = district["long_name"]
                    elif "country" in district["types"]:
                        self.address['country'] = district["long_name"]
        except:
            pass

        return super(UserLocation, self).save(*args, **kwargs)

    def __str__(self):
        return self.title




@receiver(post_save, sender=UserLocation)
def user_location_post_save(sender, *args, **kwargs):
    loc = kwargs['instance']
    if loc.is_address:
        for location in UserLocation.objects.filter(is_address=True, userProfile=loc.userProfile).exclude(pk=loc.pk):
            location.is_address = False
            location.save()


COLUMNS_STORE = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
)

BACKGROUND_COLOR = "#f9f9f9"
FONT_COLOR = "#00000"

STYLE_STORE = {
    "column": 4,
    "background_color": BACKGROUND_COLOR,
    "font_color": FONT_COLOR,
}

STATUS_STORE = (
    (0, "deactivate"),
    (1, "activate")
)


class Store(models.Model):
    logo = models.ImageField(upload_to='logo', null=False, blank=True)
    name = models.CharField(max_length=255, blank=True)
    #slug = AutoSlugField(populate_from='name', always_update=True, unique=True)
    slogan = models.TextField()
    style = JsonField(default=STYLE_STORE)
    profile = models.OneToOneField(UserProfile, unique=True, related_name='store')
    status = models.IntegerField(choices=STATUS_STORE, default=0)
    slug = models.SlugField(auto_created=True)

    def __str__(self):
        return self.name

    def clean_slug(self):
        if self.name != '':
            if Store.objects.get(slug= self.slug).count() > 0:
                raise ValidationError('Error, fields name is unique')

    def get_url(self):
        if self.slug:
            return reverse('store', args=[self.slug])
        else:
            return ''

    def save(self, *args, **kwargs):
        # Validate if has all config
        for key, value in STYLE_STORE.items():
            if not key in self.style or not self.style[key]:
                self.style[key] = value

        if self.name and not self.slug:
            from django.template.defaultfilters import slugify
            slug = slugify(self.name)
           
            while Store.objects.filter(slug=slug).count() != 0:
                slug += '1'
            
            self.slug = slug

        if self.name != '':
            self.status = 1
        else:
            self.status = 0
        return super(Store, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_config_notification(sender, *args, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        UserProfile(user=user).save()


@receiver(post_save, sender=UserProfile)
def create_config_store(sender, *args, **kwargs):
    if kwargs['created']:
        profile = kwargs['instance']
        Store(profile=profile).save()