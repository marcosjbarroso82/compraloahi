from django import forms
from .models import Ad

class AdCreateForm(forms.ModelForm):

    class Meta:
        model = Ad
        #exclude = ('slug',)

class AdModifyForm(forms.ModelForm):

    class Meta:
        model = Ad
        #exclude = ('slug',)
