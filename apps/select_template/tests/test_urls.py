from django.core.urlresolvers import reverse, resolve
from model_mommy import mommy
from test_plus.test import TestCase
from apps.users.models import Student

class TestTemplateURLs(TestCase):
    """Test URL patterns."""

    def setUp(self):
        self.student = mommy.make('Student')

    def test_single_reverse(self):
        self.assertEqual(reverse('select_template:select_for_single',kwargs={'pk':str(self.student.pk)}), '/view/'+str(self.student.pk)+'/')
            
    def test_single_reverse_basketball(self):
        self.assertEqual(reverse('select_template:basketball',kwargs={'pk':str(self.student.pk)}), '/view/basketball/'+str(self.student.pk)+'/')
            
    def test_single_reverse_clean(self):
        self.assertEqual(reverse('select_template:clean',kwargs={'pk':str(self.student.pk)}), '/view/clean/'+str(self.student.pk)+'/')

    def test_multi_reverse(self):
        self.assertEqual(reverse('select_template:multi'), '/view/multi/')

    def test_multi_business_reverse(self):
        self.assertEqual(reverse('select_template:business'), '/view/multi/business/')