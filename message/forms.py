from postman.forms import WriteForm, BaseWriteForm
from django import forms
from .models import MessageChannel
from django.utils.timezone import now as datetime_now
from postman.models import Message
from ad.models import Ad

class CustomWriteForm(BaseWriteForm):
    ad_id = forms.CharField()


    def clean(self):
        self.mc = MessageChannel(sender=self.instance.sender, recipient=self.cleaned_data['recipient'], ad=Ad.objects.get(pk=self.cleaned_data['ad_id']),
                                 date=datetime_now())


        if self.mc.already_exist():
            print("no existe")
            return super(CustomWriteForm, self).clean()
        raise forms.ValidationError('Ya hay una solicitud pendiente')

    def save(self, *args, **kwargs):
        print("save")
        super(CustomWriteForm, self).save(self, *args, **kwargs)
        self.mc.save()


    class Meta(BaseWriteForm.Meta):
        fields = ('recipient', 'subject', 'body')


    """
    class Meta(BaseWriteForm.Meta):
        fields = ('body', 'ad_id')
    """