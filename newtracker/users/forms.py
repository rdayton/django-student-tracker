from django import forms
from newtracker.users.models import Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class StudentSearchForm(forms.models.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentSearchForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('submit', 'Submit', css_class='center-block'))

    class Meta:
        model = Student
        fields = {'gpa'}

