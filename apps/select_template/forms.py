from __future__ import absolute_import

from django import forms
from apps.users.models import Student
from tinymce.widgets import TinyMCE
from django.shortcuts import get_object_or_404
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class StoryForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['story']
    
    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
       
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
    
    def clean(self):
        cleaned_data = super(StoryForm, self).clean()        
        print('cleaning')        
        return cleaned_data