from selenium import webdriver
import unittest
from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from model_mommy import mommy
from newtracker.users.models import Student
from django.conf import settings
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 5

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
    

    def wait(fn):
        def modified_fn(*args, **kwargs):  
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)  
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.1)
        return modified_fn

    @wait
    def wait_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_table')          
        self.assertIn(row_text, table.text)
                
    @wait
    def wait_for(self, fn):
        return fn()

    @wait
    def wait_to_be_logged_in(self, name):
        self.browser.find_element_by_link_text('Log out')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(name, navbar.text)
    
    def get_gpa_input_box(self):
        return self.browser.find_element_by_id('id_gpa')
    
    def setUp(self):
        self.browser = webdriver.Chrome()  
        if 'localhost' in self.server_url:    
            self.student = mommy.make('Student', gpa=3.5)
        #print(self.student)
       # self.student.save()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    