from django import template

register = template.Library()


@register.filter(name='hours')
def hours(string):
    return "Hours-" + str(string)
