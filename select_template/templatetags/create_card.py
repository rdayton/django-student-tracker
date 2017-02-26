from django import template

register = template.Library()

@register.inclusion_tag('create_card.html')
def create_card( id, template_name ,title):
    return { 'id': id, 'template_name':template_name,'title':title}

@register.inclusion_tag('select_template/create_multi_card.html')
def create_multi_card( ids, template_name ,title):
    return { 'ids': ids, 'template_name':template_name,'title':title}
