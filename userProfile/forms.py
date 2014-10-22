from django import forms
from django.forms.models import inlineformset_factory

from .models import UserProfile, Phone, UserLocation


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']
        required = ['first_name', 'last_name']
        excluded = ('user',)


Phone_inline_formset = inlineformset_factory(
    UserProfile, Phone, extra=0, min_num=1,  can_delete=True)

Location_inline_formset = inlineformset_factory(UserProfile, UserLocation, extra=0, min_num= 1, can_delete=True)