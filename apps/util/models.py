from django.db import models


class Interested(models.Model):
    email = models.EmailField(blank=False, unique=True)
    seller = models.BooleanField(default=False)
    buyer = models.BooleanField(default=False)
    android = models.BooleanField(default=False)
    ios = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class CounterWhered(models.Model):
    whered = models.CharField(max_length=100, unique=True)
    counter = models.IntegerField()

    def __str__(self):
        return self.whered



class GenericModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']