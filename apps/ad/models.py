from django.db import models

class AdQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Ad(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default=True)
    # imagen. fileupload.
    # tags []
    # price (moneda)
    # author. foreingkey.

    objects = AdQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ["-created"]

class AdImage(models.Model):
    ad_id = models.ForeignKey(Ad, related_name='images')
    image = models.ImageField(upload_to='ad')