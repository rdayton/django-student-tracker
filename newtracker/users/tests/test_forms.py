from django.test import TestCase

from newtracker.users.forms import StudentSearchForm
from crispy_forms.utils import render_crispy_form
class StudentFormTest(TestCase):
    
    def test_form_renders_students_text_input(self):
        form = StudentSearchForm()
        self.assertIn('form-control', render_crispy_form(form))

    def test_form_validation_for_blank_items(self):
        form = StudentSearchForm(data={'gpa': ''})
        self.assertFalse(form.is_valid())

    def test_form_valid(self):
        form = StudentSearchForm(data={'gpa':4.0})
        self.assertTrue(form.is_valid())