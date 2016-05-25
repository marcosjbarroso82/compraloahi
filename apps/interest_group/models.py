import random
import string

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify

from apps.util.models import GenericModel


class InterestGroup(GenericModel):
    name = models.CharField(max_length=20, unique=True)
    short_description = models.TextField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User)
    header_image = models.ImageField(default='group/header/default.png', upload_to='group/header/')
    image = models.ImageField(default='group/default.png', upload_to='group')
    slug = models.SlugField(auto_created=True, editable=False)

    def clean_slug(self):
        if self.name != '':
            #TODO: y esto? no parece estar bien!
            if InterestGroup.objects.get(slug= self.slug).count() > 0:
                raise ValidationError('Error, fields name is unique')

    def get_url(self):
        if self.slug:
            return reverse('group', args=[self.slug])
        else:
            return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)


    def __str__(self):
        return self.name


SUSCRIPTION_STATUS = (
    (0, 'A la espera'),
    (1, 'Aceptada'),
    (2, 'Rechazada'),
    (3, 'Expirada')
)



class Suscription(GenericModel):
    email = models.EmailField()
    hash_invitation = models.TextField()
    status = models.IntegerField(choices=SUSCRIPTION_STATUS, default=0)
    group = models.ForeignKey(InterestGroup, related_name='suscriptions')

    def __str__(self):
        return self.email

    def create(self, email, group):
        self.email = email
        self.hash_invitation = ''.join(random.choice(string.ascii_uppercase + string.digits) for n in range(50))
        self.group = group
        return self.save()


@receiver(post_save, sender=InterestGroup)
def group_post_save(sender, *args, **kwargs):
    if kwargs['created']:
        group = kwargs['instance']
        profile = group.owner.profile
        profile.interest_groups.add(group)
        profile.save()


@receiver(post_save, sender=Suscription)
def suscription_post_save(sender, *args, **kwargs):
    if kwargs['created']:
        suscription = kwargs['instance']

        content = """
            Has recibido una invitacion para unirte al grupo de %s , ingresa al siguiente enlase para aceptar
            http://compraloahi.com.ar/%s
        """ %(suscription.group.name, reverse('group:invitation', kwargs={'group_id': suscription.group.id, 'hash': suscription.hash_invitation}))

        msg = EmailMultiAlternatives('Compraloahi - Notifications',
                                          content,
                                          'notificacion@compraloahi.com.ar',
                                          [suscription.email])
        msg.attach_alternative(content, 'text/html')
        msg.send()
        #Notification(email=suscription, type='suscription', message=msg,
        #             extras={"url": '/suscription/%s' % suscription.hash_invitation, }).save()


class Post(GenericModel):
    group = models.ForeignKey(InterestGroup, related_name='posts')
    user = models.ForeignKey(User, related_name='posts')
    content = models.TextField()

