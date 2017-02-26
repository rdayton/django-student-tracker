from django import template

register = template.Library()

@register.inclusion_tag('create_card.html')
def create_card( id, template_name ,title):
    return { 'id': id, 'template_name':template_name,'title':title}

@register.inclusion_tag('create_multi_card.html')
def create_multi_card(  template_name, ids,title):
    return { 'ids': ids, 'template_name':template_name,'title':title}
