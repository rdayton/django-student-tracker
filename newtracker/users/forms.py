from django import forms
from newtracker.users.models import Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django.core.exceptions import ValidationError

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

class StudentSearchForm(forms.models.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentSearchForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.fields['gpa'].required = False
        # You can dynamically adjust your layout
        self.helper.layout = Layout(
        Fieldset(
            'Search Students',
            'gpa',
            'major',            
            )
        )
        self.helper.layout.append(Submit('submit', 'Submit', css_class='center-block'))

    class Meta:
        model = Student
        fields = {'gpa', 'major'}

    def clean(self):
        cleaned_data = super(StudentSearchForm, self).clean()        

        if not (self.cleaned_data.get('gpa') or self.cleaned_data.get('major')):
            raise forms.ValidationError("You must enter at least one field")
        return cleaned_data