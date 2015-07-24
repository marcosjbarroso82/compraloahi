from django.db import models
from django.contrib.comments.models import Comment
from django.contrib.auth.models import User
from django_comments_xtd.models import XtdComment
from apps.ad.models import Ad


class CommentNotification(models.Model):
    type = models.TextField(unique=False, max_length=20)
    message = models.TextField(unique=False)
    created = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad)
    receiver = models.ForeignKey(User)
    xtd_comment = models.ForeignKey(XtdComment, related_name='xtd_comment_notifications', null=True, blank=True)

    def __str__(self):
        return self.message
