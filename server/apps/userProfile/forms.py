from django import forms
from django.forms.models import inlineformset_factory

from .models import UserProfile, Phone, UserLocation


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=60, label='First Name')
    last_name = forms.CharField(max_length=60, label='Last Name')
    class Meta:
        model = UserProfile
        fields = ['image', 'birth_date']
        excluded = ('user',)


Phone_inline_formset = inlineformset_factory(
    UserProfile, Phone, extra=0, min_num=1,  can_delete=True)

Location_inline_formset = inlineformset_factory(UserProfile, UserLocation, extra=0, min_num= 1, max_num=1, can_delete=True)