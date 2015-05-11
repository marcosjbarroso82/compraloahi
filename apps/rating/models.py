from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from apps.message.models import MessageChannel

try:
    from django.contrib.contenttypes.generic import GenericForeignKey
except:
    from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.contenttypes.models import ContentType


from apps.notification.models import Notification

from .managers import RatingManager

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

CHOICES_STATUS = (
    (0, "Pendiente"),
    (1, "Aceptado"),
    (2, "Anulado")
)

CHOICES_VOTING = (
    (1, "Very bad"),
    (2, "Bad"),
    (3, "Medium"),
    (4, "Good"),
    (5, "Very Good")
)

class OverallRating(models.Model):
    user = models.ForeignKey(USER_MODEL, related_name="user_rating", unique=True)
    rate = models.DecimalField(decimal_places=1, max_digits=6, null=True)

    @classmethod
    def update(self, rating):
        try:
            o_rating = OverallRating.objects.get(user=rating.voted)
            o_rating.rate = Rating.objects.rating_all_by_user(rating.voted)
            o_rating.save()
        except OverallRating.DoesNotExist:
            OverallRating(user=rating.voted, rate=Rating.objects.rating_all_by_user(rating.voted)).save()
        except:
            print("ALGO ANDA MAL")


class Rating(models.Model):
    transaction_type = models.ForeignKey(ContentType)
    transaction_id = models.PositiveIntegerField()
    transaction_object = GenericForeignKey('transaction_type', 'transaction_id')

    state = models.IntegerField(choices=CHOICES_STATUS, default=0)
    rate = models.PositiveIntegerField(null=True, choices=CHOICES_VOTING)
    created = models.DateTimeField(auto_now_add=True)
    voted = models.ForeignKey(USER_MODEL, related_name="user_voted")
    voter = models.ForeignKey(USER_MODEL, related_name="user_voter")

    objects = RatingManager.as_manager()


@receiver(post_save, sender=Rating)
def notification_to_calification(sender, *args, **kwargs):
    """
        Created notification when created calification.
    """
    rating = kwargs['instance']
    if kwargs['created']:

        url = "www.compraloahi.com.ar" + reverse('rating:califications', kwargs={"pk": rating.id})
        message = 'Califica al usuario accediendo a ' + url
        Notification(receiver=rating.voter, type='cal', message=message, extras={'user': rating.voted.id, 'url': url }).save()
    else:
        OverallRating.update(rating=rating)


@receiver(post_save, sender=MessageChannel)
def init_rating(sender, *args, **kwargs):
    """
        Created instance rating when update status transaccion approved
    """
    if not kwargs['created']:
        message_channel = kwargs['instance']
        if message_channel.status == 'appr' and Rating.objects.exists_rating(message_channel):
            try:
                # Rating.objects.bulk_create([
                #     Rating(transaction_object=message_channel, voted=message_channel.sender, voter=message_channel.recipient),
                #     Rating(transaction_object=message_channel, voted=message_channel.recipient, voter=message_channel.sender)
                # ])
                Rating(transaction_object=message_channel, voted=message_channel.sender, voter=message_channel.recipient).save()
                Rating(transaction_object=message_channel, voted=message_channel.recipient, voter=message_channel.sender).save()
            except:
                print(message_channel)

