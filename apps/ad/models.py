import datetime

from autoslug import AutoSlugField

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver

from taggit.managers import TaggableManager

from apps.favorite.models import Favorite


class AdQuerySet(models.QuerySet):

    def published(self):
        return self.filter(status=1)


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


STATUS_AD = (
    (0, 'Delete'),
    (1, 'Active'),
    (2, 'Inactive')
)

class Ad(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', unique_with='pub_date')
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(User, related_name='ads')
    categories = models.ManyToManyField(Category)

    status = models.IntegerField(choices=STATUS_AD, default=2)

    short_description = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(default='0.00',
                                decimal_places=2,
                                max_digits=10)

    store_published = models.BooleanField(default=False)

    objects = AdQuerySet.as_manager()

    def show_location(self):
        return self.author.profile.privacy_settings.get('show_address')

    def get_user_loc(self):
        return self.author.profile.locations.filter(is_address=True).first()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ["-created"]

    def is_new(self):
        if (self.pub_date.date() + datetime.timedelta(days=30)) >= datetime.date.today():
            return True
        else:
            return False

    def delete(self, using=None, secure=False):
        if secure:
            return super(Ad, self).delete(using)
        else:
            self.status = 0
            return self.save()

    def is_favorite(self, user):
        if Favorite.objects.get_favorite(user, self):
            return True
        else:
            return False

@receiver(post_save, sender=Ad)
def ad_post_save(sender, *args, **kwargs):
    ad = kwargs['instance']

    for tag in ad.title.split(' '):
        ad.tags.add(tag)


class AdImage(models.Model):
    ad = models.ForeignKey(Ad, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ad', null=False, blank=False, )
    default = models.BooleanField(default=False)



@receiver(post_save, sender=AdImage)
def ad_image_post_save(sender, *args, **kwargs):
    image = kwargs['instance']
    if image.ad.status == 2:
        image.ad.status = 1
        image.ad.save()
    if image.default and image.ad:
        for img in AdImage.objects.filter(default=True, ad=image.ad).exclude(pk=image.pk):
            img.default = False
            img.save()


@receiver(post_delete, sender=AdImage)
def ad_image_post_delete(sender, *args, **kwargs):
    image = kwargs['instance']
    if not len(AdImage.objects.filter(ad=image.ad).exclude(pk=image.pk)):
        image.ad.status = 2
        image.ad.save()

#@receiver(pre_delete, sender=AdImage)
#def adImage_delete(sender, instance, **kwargs):
#    # Pass false so FileField doesn't save the model.
#    instance.image.delete(False)
