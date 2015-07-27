from .models import Notification

from django.dispatch import receiver
from django.db.models.signals import post_save
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
