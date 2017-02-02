from django.test import RequestFactory
from test_plus.test import TestCase
from newtracker.users.models import User
import unittest
from newtracker.views import home_page

from ..views import (
    UserRedirectView,
    UserUpdateView
)
from django.http.request import HttpRequest
from django.template.loader import render_to_string


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

class TestUserSave(BaseUserTestCase):
    def test_user_gets_saved(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['name_input'] = 'Bob'
        
        response = home_page(request)
        users = User.objects.all()
        self.assertEqual(users.count(),2)
        
        self.assertIn('Bob', response.content.decode())
        
        #TODO: Possibly doesn't load stylesheets, check later
        #expected_html = render_to_string('pages/home.html', {'name_input':'Bob'})
        #self.assertEqual(response.content.decode(), expected_html)