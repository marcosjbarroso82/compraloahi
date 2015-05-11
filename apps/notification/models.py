from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now as datetime_now

from django.dispatch import receiver
from django.db.models.signals import post_save

import ast

from push_notifications.models import GCMDevice
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
#from jsonfield import JSONField
#from django_pgjson.fields import JsonField



AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

TYPE_NOTIFICATION = (
                ('msg', 'Message'),
                ('fav', 'Favorite'),
                ('cmmt', 'Comment'),
                ('prox', 'Near Favorite'),
                ('cal', "Calification")
            )

CANAL_NOTIFICATION = (
    ('alert', 'Alert'),
    ('email', "Email")
)

CONFIG = {
    "msg": { "alert": True, "email": True },
    "fav": { "alert": True, "email": True },
    "cmmt": { "alert": True, "email": True },
    "prox": { "alert": True, "email": True },
    "cal": { "alert": True, "email": True }
}


class ConfigNotification(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='config_notifications')
    config = models.TextField()

    def save(self, *args, **kwargs):
        self.config =  str(self.config) # When change extras fields to json, remove this
        super(ConfigNotification, self).save(*args, **kwargs)

    def has_perm(self, type, canal):
        return ast.literal_eval(self.config).get(type, {}).get(canal, True)


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
        return ast.literal_eval(self.extras).get('user', "")

    def get_object_id(self):
        return ast.literal_eval(self.extras).get('id', 0)

    def get_url(self):
        return ast.literal_eval(self.extras).get('url', "")


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

            try:
                # TODO: Caputar error : GCMError: {'failure': 1, 'canonical_ids': 0, 'multicast_id': 7630349632432802077, 'results': [{'error': 'NotRegistered'}], 'success': 0}
                print("Enviando alerta.....")
                devices = GCMDevice.objects.filter(user= notification.receiver)
                devices.send_message(notification.message , extra={'type': notification.type , 'id': notification.get_user()})
                print("Alerta enviada!")
            except:
                print("Error al intentar enviar alerta")

        if config and config.has_perm(notification.type, 'email'):
            print("Enviando email.....")
            html_content = notification.message
            msg = EmailMultiAlternatives('Compraloahi - Notifications',
                                              html_content,
                                              'testnubiquo@gmail.com',
                                              [notification.receiver.email])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
            print("Email enviado!")


@receiver(post_save, sender=User)
def create_config_notification(sender, *args, **kwargs):

    if kwargs['created']:
        user = kwargs['instance']
        ConfigNotification(user=user, config=CONFIG).save()


