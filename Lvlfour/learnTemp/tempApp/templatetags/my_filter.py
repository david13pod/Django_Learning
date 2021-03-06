from django import template

register=template.Library()

@register.filter(name='cutter')
def cutter (value,arg):
    return value.replace(arg,'')

