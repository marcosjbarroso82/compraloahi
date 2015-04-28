from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now as datetime_now

from django.dispatch import receiver
from django.db.models.signals import post_save

import ast

from push_notifications.models import GCMDevice

#from jsonfield import JSONField
#from django_pgjson.fields import JsonField

from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

TYPE_NOTIFICATION = (
                ('msg', 'Message'),
                ('fav', 'Favorite'),
                ('cmmt', 'Comment'),
                ('prox', 'Near Favorite')
            )

CANAL_NOTIFICATION = (
    ('alert', 'Alert'),
    ('email', "Email")
)

CONFIG = {
    "msg": { "alert": True, "email": True },
    "fav": { "alert": True, "email": True },
    "cmmt": { "alert": True, "email": True },
    "prox": { "alert": True, "email": True }
}


class ConfigNotification(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='config_notifications')
    config = models.TextField()

    def save(self, *args, **kwargs):
        self.config =  str(self.config) # When change extras fields to json, remove this
        super(ConfigNotification, self).save(*args, **kwargs)

    def has_perm(self, type, canal):
        return ast.literal_eval(self.config).get(type, {}).get(canal, False)


class NotificationManager(models.QuerySet):

    def unread(self):
        return self.filter(read= None)

    def mark_all_read(self):
        """
            Mark all unread notification readed
        """
        date = datetime_now()
        return self.unread().update(read= date)


class Notification(models.Model):
    type = models.CharField(max_length=20, choices=TYPE_NOTIFICATION)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    receiver = models.ForeignKey(User)
    extras = models.TextField()
    #extras = models.JsonField # Implement fields json with postgres
    read = models.DateTimeField(blank=True, null=True)

    objects = NotificationManager.as_manager()

    def marked_read(self):
        if not self.read:
            self.read = datetime_now()
            self.save()

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        self.extras =  str(self.extras) # When change extras fields to json, remove this
        super(Notification, self).save(*args, **kwargs)

    def get_user(self):
        return ast.literal_eval(self.extras).get('user')

    def get_object_id(self):
        return ast.literal_eval(self.extras).get('id', 0)


@receiver(post_save, sender=Notification)
def notification_post_save(sender, *args, **kwargs):
    notification = kwargs['instance']
    if kwargs['created']:
        # Send notification
        try:
            config = ConfigNotification.objects.get(user=notification.receiver)
        except:
            config = None

        if config and config.has_perm(notification.type, 'alert'):
            device = GCMDevice.objects.filter(user= notification.receiver).first()
            device.send_message(notification.message , extra={'type': notification.type , 'id': notification.get_user()})

        if config and config.has_perm(notification.type, 'email'):
            pass
            # SEND EMAIL...



@receiver(post_save, sender=User)
def create_config_notification(sender, *args, **kwargs):

    if kwargs['created']:
        user = kwargs['instance']
        ConfigNotification(user=user, config=CONFIG).save()


