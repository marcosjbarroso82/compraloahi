from django.db import models
from django.contrib.auth.models import User


TYPE_PHONE = (
    ('Telelefono', 'Telefono'),
    ('Celular', 'Celular'),
    ('Fax', 'Fax'),
)


class UserProfile(models.Model):
    image = models.ImageField(upload_to='profile', null=False, blank=False, default="profile/images.jpg")
    birth_date = models.DateField()
    user = models.OneToOneField(User, unique=True)
    #phones = models.ManyToOneRel(Phone)

    def __str__(self):
        return 'profile ' + self.user.username

class Phone(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=200)
    userProfile = models.ForeignKey(UserProfile, related_name='phones')


class UserLocation(models.Model):
    title = models.CharField(max_length=40)
    userProfile = models.ForeignKey(UserProfile, related_name='locations')
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    radius = models.IntegerField(default=5000)

    def __str__(self):
        return self.title