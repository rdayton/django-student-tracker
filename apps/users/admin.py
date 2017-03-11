# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, Student,Hobby, AreaOfInterest, MiscAccomplishment, Employee, Employer,\
    Competition, MagnetProgram, FuturePlan, Review, Task, \
     Project, Activity, School, Quote

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Quote)
admin.site.register(Hobby)
admin.site.register(MiscAccomplishment)
admin.site.register(AreaOfInterest)
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Competition)
admin.site.register(MagnetProgram)
admin.site.register(FuturePlan)
admin.site.register(Review)
admin.site.register(Task)
#admin.site.register(Teacher)
#admin.site.register(ProfessionalOfficeEmployee)
admin.site.register(Project)
admin.site.register(Activity)

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
            ('User Profile', {'fields': ('name',)}),
    ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'name', 'is_superuser')
    search_fields = ['name']
