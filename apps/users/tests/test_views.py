from django.test import RequestFactory
from test_plus.test import TestCase
from apps.users.models import User, Student
import unittest
from apps.views import home_page, is_number
from django.db import transaction
from model_mommy import mommy
from django.template.loader import render_to_string
from django.test import Client
from apps.users.forms import StudentSearchForm

from ..views import (
    UserRedirectView,
    UserUpdateView
)
from django.http.request import HttpRequest
from django.template.loader import render_to_string
from _sqlite3 import IntegrityError
from django.test.testcases import TransactionTestCase


class BaseUserTestCase(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()


class TestUserRedirectView(BaseUserTestCase):

    def test_get_redirect_url(self):
        # Instantiate the view directly. Never do this outside a test!
        view = UserRedirectView()
        # Generate a fake request
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        view.request = request
        # Expect: '/users/testuser/', as that is the default username for
        #   self.make_user()
        self.assertEqual(
            view.get_redirect_url(),
            '/users/testuser/'
        )


class TestUserUpdateView(BaseUserTestCase):

    def setUp(self):
        # call BaseUserTestCase.setUp()
        super(TestUserUpdateView, self).setUp()
        # Instantiate the view directly. Never do this outside a test!
        self.view = UserUpdateView()
        # Generate a fake request
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        self.view.request = request

    def test_get_success_url(self):
        # Expect: '/users/testuser/', as that is the default username for
        #   self.make_user()
        self.assertEqual(
            self.view.get_success_url(),
            '/users/testuser/'
        )

    def test_get_object(self):
        # Expect: self.user, as that is the request's user object
        self.assertEqual(
            self.view.get_object(),
            self.user
        )

class TestStudentCreation(BaseUserTestCase, TransactionTestCase):
    def test_user_gets_saved(self):
        name= 'Bob'
        gpa = 4.0
        grade = 11
        user = User.objects.create(first_name=name)
        user.save()
        
        try:
            with transaction.atomic():
                student = Student.objects.create(user=user, gpa=gpa,grade_level=grade)
                student.save()
                self.assertEqual(Student.objects.all().count(), 1)
        except IntegrityError:
            user.delete()
        

class TestGPASearch(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()

    def test_home_page_uses_student_search_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], StudentSearchForm)

    def test_can_filter_by_gpa(self):
        student = mommy.make('Student', gpa=4.2)
        #view = HttpRequest()
        #self.factory = RequestFactory()
        #request = self.factory.post('/','gpa_input','4.0')
        c = Client()
        response = c.post('/',{'gpa':'4.0', 'submit':'search'})

        
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(student.gpa), response.content.decode('utf8'))
        
   
#TODO: Possibly doesn't load stylesheets, check later        