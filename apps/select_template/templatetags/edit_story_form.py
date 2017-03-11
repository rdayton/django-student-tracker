from django import template

register = template.Library()

@register.inclusion_tag('edit_story_form.html')
def show_all_from_field( student, form):
    return { 'student':student, 'form':form }

@register.inclusion_tag('story_modal_button.html')
def show_modal_button( pk):
    return { 'pk':pk}