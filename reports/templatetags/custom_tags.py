from django import template

register = template.Library()

@register.filter(name='sub')
def sub(value,args):
  return value-args
