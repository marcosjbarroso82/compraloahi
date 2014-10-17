from django import forms
from django.forms.models import inlineformset_factory

from .models import Ad, AdImage

from adLocation.models import AdLocation


class CreateAdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ('title', 'body', 'slug', 'tags')
        excluded = ('author', 'modified', 'pub_date', 'created', 'published')


class AdModifyForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ('title', 'body', 'slug', 'tags')
        excluded = ('author', 'modified', 'pub_date', 'created', 'published')


AdImage_inline_formset = inlineformset_factory(
    Ad, AdImage, extra=1, can_delete=True)
AdLocation_inline_formset = inlineformset_factory(
    Ad, AdLocation, extra=0, can_delete=False, max_num=1, min_num=1)
