from django import template

register = template.Library()

@register.inclusion_tag('show_all_from_field.html')
def show_all_from_field( title, field):
    return { 'title':title, 'field':field}

