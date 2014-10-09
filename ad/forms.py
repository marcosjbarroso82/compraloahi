from django import forms
from .models import Ad


class CreateAdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ('title', 'body', 'slug', 'tags')
        excluded = ('author', 'modified', 'pub_date', 'created', 'published')


class AdModifyForm(forms.ModelForm):

    class Meta:
        model = Ad
        #exclude = ('slug',)
