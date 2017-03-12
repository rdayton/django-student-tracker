from django import template
register = template.Library()
from apps.users.helpers import get_profile_class
from apps.users.models import ActivityStatus

@register.inclusion_tag('get_unapproved_count.html')
def get_unapproved_count(profile):   
    profile_class = get_profile_class(profile)
    if profile_class is not None:
        count = ActivityStatus.get_unapproved(profile_class).count()
        return {'count': count, 'pk':profile_class.pk }