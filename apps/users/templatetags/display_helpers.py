from django import template
register = template.Library()
from apps.users.helpers import get_profile_class
from apps.users.models import Activity

@register.inclusion_tag('get_unapproved_count.html')
def get_unapproved_count(profile):   
         
    count = Activity.objects.filter(assigned_approver=get_profile_class(profile), approved=False).count()
    return {'count': count}