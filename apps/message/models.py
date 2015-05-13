from django.db import models
from django.contrib.auth.models import User

from apps.ad.models import Ad


STATUS_CHOICES =(
    ("des", "desactivated"),
    ("pen", 'pending'),
    ("ter", "terminated"),
    ("exp", "expired"),
    ("appr", "approved"),
    ("rej", "rejected")
)
#(('des', 'desactivated'), ('act', 'activated'),('exp', 'expired'))


class MessageChannel(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    recipient = models.ForeignKey(User, related_name='recipient')
    status = models.CharField(max_length=20 ,choices=STATUS_CHOICES, default='act')
    date = models.DateField(auto_created=True, null=True)
    ad = models.ForeignKey(Ad)

    def __str__(self):
        return str(self.sender) + ' ' + str(self.recipient) + ' ' + self.status + ' ' + str(self.ad.id)

    def already_exist(self):
        print("already exits")
        len1 = len(MessageChannel.objects.filter(sender=self.sender, recipient=self.recipient, status="des", ad=self.ad))
        print(len1)
        if len1  > 0:
            return False
        else:
            return True


