from test_plus.test import TestCase
from model_mommy import mommy
from newtracker.users.models import Student
class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            'testuser'  # This is the default username for self.make_user()
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_student(self):
        self.student = mommy.make('Student')
        firststudent = Student.objects.all().first()
        self.assertEqual(self.student.__str__(), firststudent.__str__())
