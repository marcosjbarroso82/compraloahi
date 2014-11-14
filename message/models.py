from django.db import models

from django.contrib.auth.models import User

from ad.models import Ad

class MessageChannel(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    recipient = models.ForeignKey(User, related_name='recipient')
    status = models.CharField(max_length=20 ,choices=(('des', 'desactivated'), ('act', 'activated'),
                                       ('exp', 'expired')), default='des')
    date = models.DateField(auto_created=True, null=True)
    ad = models.ForeignKey(Ad)

    def __str__(self):
        return str(self.sender) + ' ' + str(self.reciever) + ' ' + self.status

    def already_exist(self):
        if len(MessageChannel.objects.filter(sender=self.sender, recipient=self.recipient).exclude(status='des')) > 0:
            return True
        else:
            return False