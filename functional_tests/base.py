from selenium import webdriver
import unittest
from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from model_mommy import mommy
from newtracker.users.models import Student
from django.conf import settings

class FunctionalTest(StaticLiveServerTestCase):
    #fixtures = ['initial.json']
    #replace fixtures with model_mommy
    
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://'+arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url    

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()
    
    def setUp(self):      
        settings.CSRF_COOKIE_SECURE = False
        settings.SESSION_COOKIE_SECURE = False  
        settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        settings.DEBUG = True
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)        
        self.student = mommy.make('Student', gpa=3.5)
       # self.student.save()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    def check_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_table')          
        self.assertIn(row_text, table.text)