from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError

from autoslug import AutoSlugField

from django_pgjson.fields import JsonField


TYPE_PHONE = (
    ('TEL', 'Telefono'),
    ('CEL', 'Celular'),
    ('FAX', 'Fax'),
)

class UserProfile(models.Model):
    image = models.ImageField(upload_to='profile', null=False, blank=False, default="profile/default.jpg")
    birth_date = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, unique=True, related_name='profile')

    def __str__(self):
        return 'profile ' + self.user.username

class Phone(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=200, choices=TYPE_PHONE)
    userProfile = models.ForeignKey(UserProfile, related_name='phones')


class UserLocation(models.Model):
    title = models.CharField(max_length=100)
    userProfile = models.ForeignKey(UserProfile, related_name='locations')
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    radius = models.IntegerField(default=5000)

    def __str__(self):
        return self.title


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
    slug = AutoSlugField(populate_from='name', always_update=True)
    slogan = models.TextField()
    style = JsonField(default=STYLE_STORE)
    profile = models.OneToOneField(UserProfile, unique=True, related_name='store')
    status = models.IntegerField(choices=STATUS_STORE, default=0)

    def __str__(self):
        return self.name

    def clean_slug(self):
        print("ENTRO AL CLEAN SLUG")
        if self.name != '':
            if Store.objects.get(slug= self.slug).count() > 0:
                raise ValidationError('Error, fields name is unique')

    def save(self, *args, **kwargs):
        # Validate if has all config
        for key, value in STYLE_STORE.items():
            if not key in self.style or not self.style[key]:
                self.style[key] = value

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