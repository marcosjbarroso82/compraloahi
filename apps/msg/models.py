from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


# moderation constants
STATUS_PENDING = 'p'
STATUS_ACCEPTED = 'a'
STATUS_REJECTED = 'r'
STATUS_CHOICES = (
    (STATUS_PENDING, _('Pending')),
    (STATUS_ACCEPTED, _('Accepted')),
    (STATUS_REJECTED, _('Rejected')),)


class Msg(models.Model):
    """
    A message between a User and another User or an AnonymousUser.
    """
    SUBJECT_MAX_LENGTH = 120

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

    # objects = MessageManager()

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

    @property
    def is_replied(self):
        """Tell if the recipient has written a reply to the message."""
        return self.replied_at is not None

    def set_read(self, date):
        if not self.read_at:
            self.read_at = date
            self.save()
