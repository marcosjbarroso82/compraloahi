# From http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/#comment-1193609278
from django import template

from django.template import Library, Node, resolve_variable




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


class AddGetParameter(Node):
    def __init__(self, values):
        self.values = values

    def render(self, context):
        req = resolve_variable('request', context)
        params = req.GET.copy()
        for key, value in self.values.items():
            params[key] = value.resolve(context)
        return '?%s' %  params.urlencode()

@register.tag
def add_get(parser, token):
    pairs = token.split_contents()[1:]
    values = {}
    for pair in pairs:
        s = pair.split('=', 1)
        values[s[0]] = parser.compile_filter(s[1])
    return AddGetParameter(values)
