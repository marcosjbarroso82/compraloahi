
from postman.forms import WriteForm
from django.forms import forms
from .models import MessageChannel
from django.utils.timezone import now as datetime_now


class CustomWriteForm(WriteForm):
    ad_id = forms.TextInput()

    def clean(self):
        self.mc = MessageChannel(sender=self.instance.sender, recipient=self.instance.recipient, ad=self.instance.ad_id,
                            data=datetime_now())

        if self.mc.already_exist() is False:
            super(CustomWriteForm, self).clean(self)
        raise forms.ValidationError('Ya hay una solicitud pendiente')

    def save(self, *args, **kwargs):
        super(CustomWriteForm, self).save(self, *args, **kwargs)
        self.mc.save()