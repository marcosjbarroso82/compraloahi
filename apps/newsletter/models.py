from django.db import models


class Interested(models.Model):
    email = models.EmailField(blank=False, unique=True)
    seller = models.BooleanField(default=False)
    buyer = models.BooleanField(default=False)
    android = models.BooleanField(default=False)
    ios = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Pq(models.Model):
    identification = models.CharField()
    whereis = models.CharField()
    counter = models.IntegerField()

    def __str__(self):
        return self.whereis

