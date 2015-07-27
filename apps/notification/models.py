from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now as datetime_now

from django.dispatch import receiver
from django.db.models.signals import post_save

from push_notifications.models import GCMDevice
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from django_pgjson.fields import JsonField


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

CONFIG_NOTIFICATION = {
    "msg": { "alert": True, "email": True, "label": "Desea recibir una notificacion cuando recibe un mensaje"},
    "fav": { "alert": True, "email": True, "label": "Desea recibir una notificacion cuando agregan un aviso propio a favoritos" },
    "cmmt": { "alert": True, "email": True, "label": "Desea recibir una notificacion cuando commentan un aviso propio" },
    "prox": { "alert": True, "email": True, "label": "Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos" },
    "cal": { "alert": True, "email": True, "label": "Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario" }
}


class ConfigNotification(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='config_notifications', unique=True)
    config = JsonField(default=CONFIG_NOTIFICATION)

    def save(self, *args, **kwargs):
        # Validate if has all config
        for config in CONFIG_NOTIFICATION.keys():
            for key, value in CONFIG_NOTIFICATION[config].items():
                if not self.config[config] or not key in self.config[config] or key == 'label':
                    self.config[config][key] = value

        super(ConfigNotification, self).save(*args, **kwargs)

    def has_perm(self, type, canal):
        if self.config[type][canal]:
            return True
        else:
            return False




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
    extras = JsonField()
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

    def get_user(self):
        return self.extras.get('user', "")

    def get_object_id(self):
        return self.extras.get('id', 0)

    def get_url(self):
        return self.extras.get('url', "")


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
            url = notification.extras.get('url')
            if url:
                html_content = notification.message + "\b" + "Ingresa a el siguiente link para ver la notificacion http:://compraloahi.com.ar/" + url
            else:
                html_content = notification.message
            msg = EmailMultiAlternatives('Compraloahi - Notifications',
                                              html_content,
                                              'notification@compraloahi.com.ar',
                                              [notification.receiver.email])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
            print("Email enviado!")


@receiver(post_save, sender=User)
def create_config_notification(sender, *args, **kwargs):

    if kwargs['created']:
        user = kwargs['instance']
        ConfigNotification(user=user, config=CONFIG_NOTIFICATION).save()


#TODO: De aca para abajo hay que eliminarlo cuando se pueda ejecutar el archivo receiver de este modulo
from apps.ad.models import Ad
from django_comments_xtd.models import XtdComment


@receiver(post_save, sender=XtdComment, dispatch_uid='XTDCommentPostSave')
def handle_xtd_comment_post_save(sender, *args, **kwargs):
    comment = kwargs['instance']
    if (comment.level == 0 and not kwargs['created']):

        ad = Ad.objects.get(pk=comment.object_pk)
        url =  'ad/' + str(ad.slug) + '/'

        Notification(receiver=ad.author, type='cmmt', message="Nuevo comentario en el aviso " + str(ad.title),
                     extras={"comment": str(comment), "url": url, "ad": comment.object_pk }).save()


