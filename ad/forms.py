from django import forms
#from django.forms.models import BaseInlineFormSet
from django.forms.models import inlineformset_factory

from .models import Ad, AdImage


class CreateAdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ('title', 'body', 'slug', 'tags')
        excluded = ('author', 'modified', 'pub_date', 'created', 'published')


class AdModifyForm(forms.ModelForm):

    class Meta:
        model = Ad
        #exclude = ('slug',)

"""
class InlineAdImageForm(BaseInlineFormSet):

    class Meta:
        model = AdImage
"""

AdImage_inline_formset = inlineformset_factory(Ad, AdImage, extra=1)
