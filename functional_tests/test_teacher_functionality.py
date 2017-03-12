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
       
        self.browser.find_element_by_id('log-in-link').click()
        self.browser.find_element_by_id('id_login').send_keys('lbird')
        self.browser.find_element_by_id('id_password').send_keys('password#1'+Keys.ENTER)


        # He notices he has 1 event awaiting his approval
        self.assertIn('1', self.browser.find_element_by_id('unapproved-count').text)

        # He clicks the notification
        self.browser.find_element_by_id('unapproved-count').click()

        # He is taken to the approvals page
        self.assertIn('approve',self.browser.current_url) 