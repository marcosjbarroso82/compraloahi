from postman.forms import BaseWriteForm
from django import forms
from django.utils.timezone import now as datetime_now

from .models import MessageChannel
from apps.ad.models import Ad


class CustomWriteForm(BaseWriteForm):
    ad_id = forms.CharField(widget=forms.TextInput(attrs={'hidden':'True'}))

    def clean(self):
        ad = Ad.objects.get(pk=self.cleaned_data['ad_id'])
        self.instance.recipient = ad.author

        self.mc = MessageChannel(sender=self.instance.sender, recipient=ad.author, ad= ad,
                                 date=datetime_now())

        if self.mc.already_exist():
            return super(CustomWriteForm, self).clean()
        raise forms.ValidationError('Ya hay una solicitud pendiente')


    def clean_recipients(self):
        """Check no filter prohibit the exchange."""
        recipients = []
        recipients.append(self.instance.recipient)

        return recipients


    def save(self, *args, **kwargs):
        super(CustomWriteForm, self).save(self, *args, **kwargs)
        self.mc.save()

    class Meta(BaseWriteForm.Meta):
        fields = ('subject', 'body')
        exclude = ('recipient', )
        widgets = {
            # for better confort, ensure a 'cols' of at least
            # the 'width' of the body quote formatter.
            'body': forms.Textarea(attrs={'rows': 6}),
        }
