# From http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/#comment-1193609278
from django.utils.encoding import force_text
from decimal import Decimal, InvalidOperation
from django import template
register = template.Library()
 
@register.filter(name='add_attributes')
def add_attributes(field, css):
    attrs = {}
    definition = css.split(',')
 
    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            t, v = d.split(':')
            attrs[t] = v
 
    return field.as_widget(attrs=attrs)

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})


@register.filter(name='float_decimal_part')
def floatdecimalpartformat(text, arg=-1):


    try:
        i, d = divmod(float(text), 1)
    except UnicodeEncodeError:
        return '00'

    return str(int(d * 100)).zfill(2)