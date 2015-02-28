from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.ad.models import Ad
from django_comments_xtd.models import *

from .models import *

@receiver(post_save, sender=XtdComment, dispatch_uid='XTDCommentPostSave')
def handle_xtd_comment_post_save(sender, *args, **kwargs):
    # TODO: Cuando los comentarios sean moderados, deberia ser creada la notificaion en otra parte
    comment = kwargs['instance']
    if (comment.level == 0 and not kwargs['created']):
        commentNotification = CommentNotification()
        commentNotification.type = 'not_replied'
        commentNotification.xtd_comment = comment
        commentNotification.receiver = comment.user
        commentNotification.ad = Ad.objects.get(pk=comment.object_pk)
        commentNotification.save()

