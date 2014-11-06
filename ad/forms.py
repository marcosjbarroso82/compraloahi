from django import forms
from django.forms.models import inlineformset_factory

from .models import Ad, AdImage, CategoryTag
from adLocation.models import AdLocation
from ckeditor.widgets import CKEditorWidget


class TextCheckboxSelectMultiple(forms.widgets.CheckboxSelectMultiple):
    """
    Set checked values based on a comma separated list instead of a python list
    """
    def render(self, name, value, **kwargs):
        try:
            value = list(value)
            value = [tag.tag.name for tag in value]
        except:
            value = []
        return super(TextCheckboxSelectMultiple, self).render(name, value, **kwargs)


class TextMultiField(forms.MultipleChoiceField):
    """
    Work in conjunction with TextCheckboxSelectMultiple to store a
    comma separated list of multiple choice values in a CharField/TextField
    """
    widget = TextCheckboxSelectMultiple
    def clean(self, value):
        val = super(TextMultiField, self).clean(value)
        return val


class CreateAdForm(forms.ModelForm):
    categories = TextMultiField(choices=tuple(CategoryTag.objects.all().values_list("name", "name") ) )

    class Meta:
        model = Ad
        fields = ('title', 'short_description', 'price', 'body', 'slug', 'tags', 'categories', 'pub_date')
        excluded = ('author', 'modified', 'created', 'published')
        widgets = {'body': CKEditorWidget(config_name='awesome_ckeditor')}


class AdModifyForm(forms.ModelForm):
    categories = TextMultiField(choices=tuple(CategoryTag.objects.all().values_list("name", "name")), initial="cat1")

    class Meta:
        model = Ad
        fields = ('title','short_description','price', 'body', 'slug', 'tags', "categories")
        excluded = ('author', 'modified', 'pub_date', 'created', 'published')
        widgets = {'body': CKEditorWidget(config_name='awesome_ckeditor')}

AdImage_inline_formset = inlineformset_factory(
    Ad, AdImage, extra=1, can_delete=True)
AdLocation_inline_formset = inlineformset_factory(
    Ad, AdLocation, extra=0, can_delete=False, max_num=1, min_num=1)
