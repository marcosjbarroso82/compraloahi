from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

TYPE_PHONE = (
    ('TEL', 'Telefono'),
    ('CEL', 'Celular'),
    ('FAX', 'Fax'),
)


class UserProfile(models.Model):
    image = models.ImageField(upload_to='profile', null=False, blank=False, default="profile/default.png")
    birth_date = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, unique=True, related_name='profile')

    def __str__(self):
        return 'profile ' + self.user.username

class Phone(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=200, choices=TYPE_PHONE)
    userProfile = models.ForeignKey(UserProfile, related_name='phones')


class UserLocation(models.Model):
    title = models.CharField(max_length=40)
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

class Store(models.Model):
    logo = models.ImageField(upload_to='logo', null=False, blank=False, default="logo/default.png")
    name = models.CharField(max_length=255, default="Name")
    column = models.PositiveIntegerField(choices=COLUMNS_STORE, default=4) # TODO: Field limited to config layout
    profile = models.OneToOneField(UserProfile, unique=True, related_name='store')


@receiver(post_save, sender=User)
def create_config_notification(sender, *args, **kwargs):

    if kwargs['created']:
        user = kwargs['instance']
        profile = UserProfile(user=user).save()
        Store(profile=profile).save()

