from django import template

register = template.Library()

@register.inclusion_tag('edit_story_form.html')
def show_all_from_field( student, form):
    return { 'student':student, 'form':form }

