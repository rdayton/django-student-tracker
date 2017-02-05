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
    

    def wait_for_row_in_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_table')          
                self.assertIn(row_text, table.text)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                   raise e
                time.sleep(0.1)
    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.1)
    
    def setUp(self):
        self.browser = webdriver.Chrome()  
        if 'localhost' in self.server_url:    
            self.student = mommy.make('Student', gpa=3.5)
        #print(self.student)
       # self.student.save()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    