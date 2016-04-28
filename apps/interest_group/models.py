from django.db import models
from django.contrib.auth.models import User

class InterestGroup(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(User)
    image = models.ImageField(upload_to='groups', null=False, blank=False)

    def __str__(self):
        return self.name