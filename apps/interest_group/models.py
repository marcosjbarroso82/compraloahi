import itertools
import random
import string

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify

from apps.util.models import GenericModel
from apps.notification.models import Notification

STATUS_GROUP = (
    (0, 'Active'),
    (1, 'Delete')
)

class InterestGroup(GenericModel):
    name = models.CharField(max_length=20)
    short_description = models.TextField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User)
    image_header = models.ImageField(default='group/header/default.png', upload_to='group/header/')
    image = models.ImageField(default='group/default.png', upload_to='group')
    status = models.IntegerField(choices=STATUS_GROUP, default=0)
    slug = models.SlugField(auto_created=True, editable=False, unique=True)

    # def clean_slug(self):
    #     if self.name != '':
    #         #TODO: y esto? no parece estar bien!
    #         print("VALIDATE SLUG")
    #         print(39*"===")
    #         if InterestGroup.objects.get(slug= self.slug).count() > 0:
    #             raise ValidationError('Error, fields name is unique')

    def get_url(self):
        if self.slug:
            return reverse('group:detail', args=[self.slug,])
        else:
            return ''

    def save(self, *args, **kwargs):
        self.slug = orig = slugify(self.name)

        for x in itertools.count(1):
            if not InterestGroup.objects.filter(slug=self.slug).exists():
                break
            self.slug = '%s-%d' % (orig, x)

        super(InterestGroup, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


ROLES_MEMBERS_GROUP = (
    (0, 'Admin'),
    (1, 'Member')
)

class Membership(GenericModel):
    role = models.IntegerField(choices=ROLES_MEMBERS_GROUP, default=1)
    user = models.ForeignKey(User, related_name='memberships')
    group = models.ForeignKey(InterestGroup, related_name='memberships')

    def __str__(self):
        return '%s : %s' %(self.get_role_display(), self.user.username)


REQUEST_STATUS = (
    (0, 'Pedido'), # Pedido: Cuando el usuario hace la petision de unirse
    (1, 'Preaprobado'), # Preaprobado: Cuando el admin del grupo invita a un usuario
    (2, 'Aceptado'),
    (3, 'Rechazado'), # Rechazado:
    (4, 'Expirado')
)


class MemberShipRequest(GenericModel):
    # TODO: Validar que el user o el email sean requeridos con respecto al estado
    user = models.ForeignKey(User, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    hash_validation = models.TextField(unique=True)
    status = models.IntegerField(choices=REQUEST_STATUS, default=0)
    group = models.ForeignKey(InterestGroup, related_name='membership_requests')

    def __str__(self):
        return self.email if self.email else self.user.username

    def clean(self):
        if self.user:
            if Membership.objects.get(user=self.user, group=self.group):
                raise ValidationError("The member belong to this group")

        super(MemberShipRequest, self).clean()

    def accept(self):
        if self.user:
            self.status = 2
            Membership(user=self.user, group=self.group).save()
            return self.save()

    def reject(self):
        self.status = 3
        return self.save()

    def save(self, *args, **kwargs):
        self.hash_validation = ''.join(random.choice(string.ascii_uppercase + string.digits) for n in range(50))
        # TODO: Test para saber si entra en un bucle infinito
        while MemberShipRequest.objects.filter(hash_validation=self.hash_validation):
            self.hash_validation = ''.join(random.choice(string.ascii_uppercase + string.digits) for n in range(50))

        return super(MemberShipRequest, self).save(*args, **kwargs)


@receiver(post_save, sender=MemberShipRequest)
def suscription_post_save(sender, *args, **kwargs):
    if kwargs['created']:
        membership_request = kwargs['instance']
        if membership_request.status == 1:
            url = reverse('group:invitation', kwargs={'group_id': membership_request.group.id,
                                                                 'hash': membership_request.hash_validation})
            content = """
                Has recibido una invitacion para unirte al grupo de %s , ingresa al siguiente enlase para aceptar
                http://compraloahi.com.ar%s
            """ %(membership_request.group.name, url)

            #msg = EmailMultiAlternatives('Compraloahi - Notifications',
            #                                  content,
            #                                  'notificacion@compraloahi.com.ar',
            #                                  [membership_request.email])
            #msg.attach_alternative(content, 'text/html')
            #msg.send()
            Notification(type='membership', message=content,
                         extras={"url": url, 'email': membership_request.email}).save()
    else:
        pass


class Post(GenericModel):
    group = models.ForeignKey(InterestGroup, related_name='posts')
    user = models.ForeignKey(User, related_name='posts')
    content = models.TextField()


@receiver(post_save, sender=Post)
def post_post_save(sender, *args, **kwargs):
    if kwargs['created']:
        post = kwargs['instance']
        url = post.group.get_url()
        content = """
            Se ha echo una nueva publicacion en el grupo %s.
        """ % post.group.name

        for member in post.group.memberships.all():
            Notification(receiver=member.user, type='post', message=content,
                         extras={"url": url, }).save()
