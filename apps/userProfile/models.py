from django.db import models
from django.contrib.auth.models import User


TYPE_PHONE = (
    ('TEL', 'Telefono'),
    ('CEL', 'Celular'),
    ('FAX', 'Fax'),
)


class UserProfile(models.Model):
    image = models.ImageField(upload_to='profile', null=False, blank=False)
    birth_date = models.DateField()
    user = models.OneToOneField(User, unique=True)
    #phones = models.ManyToOneRel(Phone)


class Phone(models.Model):
    number = models.IntegerField()
    type = models.CharField(choices=TYPE_PHONE, max_length=200)
    userProfile = models.ForeignKey(UserProfile, related_name='phones')


class UserLocation(models.Model):
    title = models.CharField(max_length=40)
    userProfile = models.ForeignKey(UserProfile, related_name='locations')
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.title