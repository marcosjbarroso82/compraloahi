from django.db import models
from django.contrib.auth.models import User

class InterestGroup(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name