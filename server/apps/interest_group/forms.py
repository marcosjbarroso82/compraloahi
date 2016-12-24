from django import forms
from .models import MemberShipRequest


REQUEST_STATUS = (
    (2, 'Aceptada'),
    (3, 'Rechazada')
)


class MemberShipRequestForm(forms.ModelForm):
    status = forms.ChoiceField(choices=REQUEST_STATUS, widget=forms.RadioSelect, required=True)

    class Meta:
        model = MemberShipRequest
        fields = ('status',)
