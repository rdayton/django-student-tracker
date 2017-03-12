###helpers.py
from apps.users.models import Student, Teacher, User

def get_profile_class(user):
    profile = __get_instance_or_none(Teacher, user=user)
    if profile is None:
        profile = __get_instance_or_none(Student, user=user)
    return profile

def __get_instance_or_none(model, **kwargs):
    try:
        result = model.objects.get(**kwargs)
    except:
        result = None
    return result