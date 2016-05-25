from django import forms
from .models import Suscription


SUSCRIPTION_STATUS = (
    (1, 'Aceptada'),
    (2, 'Rechazada')
)


class SuscriptionForm(forms.ModelForm):
    status = forms.ChoiceField(choices=SUSCRIPTION_STATUS, widget=forms.RadioSelect, required=True)

    class Meta:
        model = Suscription
        fields = ('status',)
