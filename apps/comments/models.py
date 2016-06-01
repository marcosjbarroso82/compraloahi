from django_comments_xtd.models import XtdComment

from apps.ad.models import Ad

from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.notification.models import Notification
from django.core.urlresolvers import reverse



@receiver(post_save, sender=XtdComment, dispatch_uid='XTDCommentPostSave')
def handle_xtd_comment_post_save(sender, *args, **kwargs):
    """
        Generate notification when comment on detail ad.
    """
    comment = kwargs['instance']
    if (comment.level == 0 and not kwargs['created']):

        ad = Ad.objects.get(pk=comment.object_pk)
        url = reverse('ad:detail', args=[ad.slug])

        Notification(receiver=ad.author, type='cmmt', message="Nuevo comentario en el aviso " + str(ad.title),
                     extras={"comment": str(comment), "url": url, "ad": comment.object_pk }).save()