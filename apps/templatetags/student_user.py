'''
from django import template

register = template.Library()

@register.inclusion_tag('users/get_student.html')
def get_student(user):
    return {'user': user}

'''