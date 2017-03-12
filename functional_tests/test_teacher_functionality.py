from .base import FunctionalTest
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys

from model_mommy import mommy
from apps.users.models import Teacher, User, Activity

class TeacherTest(FunctionalTest):

    def test_can_approve_activity(self):
        # Mr. Bird loads the site
        self.browser.get(self.server_url)
        # He logs in to his account
        # # mommy make does not correctly hash the password when creating a user so the standard create_user function is used
        teacher_user = User.objects.create_user(username='lbird',
                                                email='megan@example.com',
                                                password = 'password#1',
                                                is_active = True)
        teacher = mommy.make(Teacher, user=teacher_user)
        activity = mommy.make(Activity, assigned_approver=teacher) 
        self.browser.find_element_by_id('log-in-link').click()
        self.browser.find_element_by_id('id_login').send_keys('lbird')
        self.browser.find_element_by_id('id_password').send_keys('password#1'+Keys.ENTER)


        # He notices he has 1 event awaiting his approval
        self.assertIn('1', self.browser.find_element_by_id('unapproved-count').text)