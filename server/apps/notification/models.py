from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now as datetime_now

from push_notifications.models import GCMDevice

from django_pgjson.fields import JsonField


from django.template.loader import render_to_string


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

TYPE_NOTIFICATION = (
    ('msg', 'Message'),
    ('fav', 'Favorite'),
    ('cmmt', 'Comment'),
    ('prox', 'Near Favorite'),
    ('cal', "Calification"),
    ('membership', "Membership"),
    ('post', "GroupPost")
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
    "cal": { "alert": True, "email": True, "label": "Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario" },
    "post": { "alert": True, "email": True, "label": "Desea recibir una notificacion cuando hacen publicaciones en los grupos a los que pertenece" }
}


class ConfigNotification(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='config_notifications', unique=True)
    config = JsonField(default=CONFIG_NOTIFICATION)

    def save(self, *args, **kwargs):

        # Validate if has all config
        for check_key in CONFIG_NOTIFICATION.keys():
            if not self.config.get(check_key):
                self.config[check_key] = CONFIG_NOTIFICATION[check_key]
            for config in CONFIG_NOTIFICATION.keys():
                for key, value in CONFIG_NOTIFICATION[config].items():
                    if not self.config.get(config) or not key in self.config.get(config) or key == 'label':
                        self.config[config][key] = value

        super(ConfigNotification, self).save(*args, **kwargs)

    def has_perm(self, type, canal):
        if self.config.get(type) and self.config[type].get(canal):
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
    # TODO: Validar que el usuario o el email sea requerido (uno si o si)
    type = models.CharField(max_length=20, choices=TYPE_NOTIFICATION)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    receiver = models.ForeignKey(User, null=True)
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
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ["-created"]

    def get_user(self):
        return self.extras.get('user', "")

    def get_object_id(self):
        return self.extras.get('id', 0)

    def get_url(self):
        return self.extras.get('url', "")

    def get_email(self):
        if self.receiver and self.receiver.email:
            return self.receiver.email
        elif self.extras.get('email'):
            return self.extras.get('email')
        else:
            return None



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

                extra = notification.extras
                extra['type'] = notification.type
                extra['id'] = notification.receiver.id

                # devices.send_message(notification.message , extra={'type': notification.type , 'id': notification.receiver.id})
                devices.send_message(notification.message , extra=extra)
                print("Alerta enviada!")
            except:
                print("Error al intentar enviar alerta")

        if config and config.has_perm(notification.type, 'email') and notification.get_email():
            print("Enviando email.....")
            url = notification.get_url()
            context_data = {}

            if url:
                context_data['message'] = notification.message + "\b" + "Ingresa a el siguiente link para ver el detalle http://compraloahi.com.ar" + url
            else:
                context_data['message'] = notification.message

            message = render_to_string('notification/email.html', context_data)
            subject = '[Compraloahi] - Notificacion'
            msg = EmailMultiAlternatives(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [notification.receiver.email, ],
                )

            msg.attach_alternative(message, "text/html")
            msg.send()
            print("Email enviado!")


@receiver(post_save, sender=User)
def create_config_notification(sender, *args, **kwargs):

    if kwargs['created']:
        user = kwargs['instance']
        ConfigNotification(user=user, config=CONFIG_NOTIFICATION).save()



from apps.msg.models import Msg

@receiver(post_save, sender=Msg)
def msg_post_save(sender, *args, **kwargs):
    if(kwargs['created']):
        msg = kwargs['instance']
        if msg.thread:
            thread = msg.thread.id
        else:
            thread = msg.id
        url = '/panel/mensajes/hilo/' + str(thread)

        if msg.recipient:
            Notification(receiver=msg.recipient, type='msg', message="Tiene un nuevo mensaje",
                         extras={ "url": url, "thread": thread, 'id': msg.id }).save()
