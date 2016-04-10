from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.contenttypes import fields
from django.conf import settings
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


import datetime
# moderation constants
STATUS_PENDING = 'p'
STATUS_ACCEPTED = 'a'
STATUS_REJECTED = 'r'
STATUS_CHOICES = (
    (STATUS_PENDING, _('Pending')),
    (STATUS_ACCEPTED, _('Accepted')),
    (STATUS_REJECTED, _('Rejected')),)


from django.contrib.contenttypes.models import ContentType
# related_objec_type = ContentType.objects.get(app_label=settings.MSG_RELATED_APP_LABEL, model=settings.MSG_RELATED_MODEL)

class Msg(models.Model):
    """
    A message between a User and another User or an AnonymousUser.
    """
    SUBJECT_MAX_LENGTH = 120

    TRUE_VALUES = set(('t', 'T', 'true', 'True', 'TRUE', '1', 1, True))
    FALSE_VALUES = set(('f', 'F', 'false', 'False', 'FALSE', '0', 0, 0.0, False))

    subject = models.CharField(_("subject"), max_length=30)
    body = models.TextField(_("body"), blank=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='msg_sent_messages', null=True, blank=True,
        verbose_name=_("sender"))
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='msg_received_messages', null=True, blank=True,
        verbose_name=_("recipient"))
    parent = models.ForeignKey('self', related_name='msg_next_messages', null=True, blank=True, verbose_name=_("parent message"))
    thread = models.ForeignKey('self', related_name='msg_child_messages', null=True, blank=True, verbose_name=_("root message"))
    sent_at = models.DateTimeField(_("sent at"), auto_now_add=True)
    read_at = models.DateTimeField(_("read at"), null=True, blank=True)
    replied_at = models.DateTimeField(_("replied at"), null=True, blank=True)
    sender_archived = models.BooleanField(_("archived by sender"), default=False)
    recipient_archived = models.BooleanField(_("archived by recipient"), default=False)
    sender_deleted_at = models.DateTimeField(_("deleted by sender at"), null=True, blank=True)
    recipient_deleted_at = models.DateTimeField(_("deleted by recipient at"), null=True, blank=True)
    # moderation fields
    moderation_status = models.CharField(_("status"), max_length=1, choices=STATUS_CHOICES, default=STATUS_PENDING)
    # moderation_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='moderated_messages',
    #     null=True, blank=True, verbose_name=_("moderator"))
    moderation_date = models.DateTimeField(_("moderated at"), null=True, blank=True)
    moderation_reason = models.CharField(_("rejection reason"), max_length=120, blank=True)
    # related_obj = generic.GenericForeignKey(related_objec_type, settings.MSG_RELATED_OBJ_ID)
    # related_obj_type = ContentType.objects.get(app_label="apps.ad", model="Ad")
    # related_obj = generic.GenericForeignKey(related_obj_type, 'pk')
    # objects = MessageManager()
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    related_obj = fields.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")
        ordering = ['-sent_at', '-id']

    def is_pending(self):
        """Tell if the message is in the pending state."""
        return self.moderation_status == STATUS_PENDING
    def is_rejected(self):
        """Tell if the message is in the rejected state."""
        return self.moderation_status == STATUS_REJECTED
    def is_accepted(self):
        """Tell if the message is in the accepted state."""
        return self.moderation_status == STATUS_ACCEPTED

    @property
    def is_new(self):
        """Tell if the recipient has not yet read the message."""
        return self.read_at is None
        # return True

    @is_new.setter
    def is_new(self, value):
        if not self.read_at and value in self.FALSE_VALUES:
            self.read_at = datetime.datetime.now()
            self.save()
        elif value in self.TRUE_VALUES:
            self.read_at = None
            self.save()


    @property
    def is_replied(self):
        """Tell if the recipient has written a reply to the message."""
        return self.replied_at is not None

    @is_replied.setter
    def is_replied(self, value):
        if not self.replied_at and value in self.TRUE_VALUES:
            self.replied_at = datetime.datetime.now()
            self.save()
        elif value in self.FALSE_VALUES:
            self.replied_at = None
            self.save()

    @property
    def sender_deleted(self):
        """Tell if the recipient has written a reply to the message."""
        return self.sender_deleted_at is not None

    @sender_deleted.setter
    def sender_deleted(self, value):
        if not self.sender_deleted_at and value in self.TRUE_VALUES:
            self.sender_deleted_at = datetime.datetime.now()
            self.save()
        elif value in self.FALSE_VALUES:
            self.sender_deleted_at = None
            self.save()

    @property
    def recipient_deleted(self):
        """Tell if the recipient has written a reply to the message."""
        return self.recipient_deleted_at is not None

    @recipient_deleted.setter
    def recipient_deleted(self, value):
        if not self.recipient_deleted and value in self.TRUE_VALUES:
            self.recipient_deleted_at = datetime.datetime.now()
            self.save()
        elif value in self.FALSE_VALUES:
            self.recipient_deleted_at = None
            self.save()


@receiver(post_save, sender=Msg)
def msg_check_thread_post_save(sender, *args, **kwargs):
    if(kwargs['created']):
        msg = kwargs['instance']
        # TODO: This resolve problem with get the last message by thread on inbox.
        if not msg.thread:
            msg.thread = msg
            msg.save()
