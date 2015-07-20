from django import forms

from haystack.forms import FacetedSearchForm
from haystack.utils.geo import Point, D


class AdSearchForm(FacetedSearchForm):
    lat = forms.FloatField(required=False, label="lat")
    lng = forms.FloatField(required=False, label="lng")
    radius = forms.FloatField(required=False, label="radius")

    selected_facets = forms.CharField(required=False, widget=forms.HiddenInput)
    order_by = forms.CharField(required=False, widget=forms.HiddenInput)

    def no_query_found(self):
        return self.searchqueryset.all()

    def search(self):
        # First, store the SearchQuerySet received from other processing. (the main work is run internally by Haystack here).
        sqs = super(AdSearchForm, self).search()
        try:
            if self.cleaned_data.get('lat') and self.cleaned_data.get('lng') and self.cleaned_data.get('radius'):
                location = Point(self.cleaned_data.get('lng'), self.cleaned_data.get('lat'))
                max_dist = D(km=self.cleaned_data.get('radius')) # Un bug en haystack demanda que se multiplique por 1000. asique ahi lo esta tomando en metros
                sqs = sqs.dwithin('location', location, max_dist)

            if self.cleaned_data.get('order_by'):
                # TODO: Add support for multiple order fields
                # TODO: Add support for non-numeric field ordering ( so far only "pride" and pub_date" are working)
                order_by = self.cleaned_data.get('order_by')
                # if Search Query Set is order by distance, it might no be secure to order by any other field ( accordind to the hasytack codmumentation )
                if ( (order_by == 'distance' or order_by == '-distance')) and self.cleaned_data.get('lat') and self.cleaned_data.get('lng'):
                    location = Point(self.cleaned_data.get('lng'), self.cleaned_data.get('lat'))
                    sqs = sqs.distance('location', location).order_by(order_by)
                else:
                    sqs = sqs.order_by(order_by )

        except:
            pass
        # if something goes wrong
        if not self.is_valid():
            return self.no_query_found()

        return sqs

    def __name__(self):
        return "AdSearchForm"


# class TextCheckboxSelectMultiple(forms.widgets.CheckboxSelectMultiple):
#     """
#     Set checked values based on a comma separated list instead of a python list
#     """
#     def render(self, name, value, **kwargs):
#         try:
#             value = list(value)
#
#             value = [cat_id for cat_id in value]
#         except:
#             value = []
#         return super(TextCheckboxSelectMultiple, self).render(name, value, **kwargs)
#
#
# class TextMultiField(forms.MultipleChoiceField):
#     """
#     Work in conjunction with TextCheckboxSelectMultiple to store a
#     comma separated list of multiple choice values in a CharField/TextField
#     """
#     widget = TextCheckboxSelectMultiple
#     def clean(self, value):
#         val = super(TextMultiField, self).clean(value)
#         return val
#
#
# class CreateAdForm(forms.ModelForm):
#     # TODO: ALERT: When init migrate need comment this line
#     categories = TextMultiField(choices=tuple(Category.objects.all().values_list("id", "name")))
#
#     class Meta:
#         model = Ad
#         fields = ('title', 'short_description', 'price', 'body', 'categories')
#         excluded = ('author', 'modified', 'created', 'published', 'pub_date', 'tags' )
#         #widgets = {'body': CKEditorWidget(config_name='awesome_ckeditor'), 'pub_date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}) }
#
#
# class AdModifyForm(forms.ModelForm):
#     # TODO: ALERT: When init migrate need comment this line
#     categories = TextMultiField(choices=tuple(Category.objects.all().values_list("id", "name")))
#
#     class Meta:
#         model = Ad
#         fields = ('title','short_description','price', 'body', 'tags', 'categories')
#         excluded = ('author', 'modified', 'pub_date', 'created', 'published')
#         widgets = {'body': CKEditorWidget(config_name='awesome_ckeditor'), 'pub_date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}) }
#
#
# from django.forms.extras.widgets import Widget
#
# class AdImageForm(forms.ModelForm):
#     image = forms.ImageField(forms.ClearableFileInput(attrs={'ng-model': 'image'}))
#
#     class Meta:
#         model = AdImage
#         fields = ('image', )
#
#
# AdImage_inline_formset = inlineformset_factory(
#     Ad, AdImage, extra=1, can_delete=True, form=AdImageForm)
# AdLocation_inline_formset = inlineformset_factory(
#     Ad, AdLocation, extra=0, can_delete=False, max_num=1, min_num=1)
