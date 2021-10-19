from django import template

register = template.Library()


@register.filter
def calculate_font_size(value):
    font_size = value**(1/6)
    return int(font_size*20)
