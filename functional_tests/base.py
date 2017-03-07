from selenium import webdriver
import unittest
from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from model_mommy import mommy
from apps.users.models import Student, User, Activity, AreaOfInterest, Competition, Employee, Employer, FuturePlan, Hobby, MagnetProgram, MiscAccomplishment, Project, Quote, Review, School, Task
from django.conf import settings
from selenium.common.exceptions import WebDriverException
import time
import os
from datetime import datetime

MAX_WAIT = 5

def wait(fn):
        def modified_fn(*args, **kwargs):  
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)  
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.7)
        return modified_fn


SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
class FunctionalTest(StaticLiveServerTestCase):
    #fixtures = ['initial.json']
    #replace fixtures with model_mommy
    
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://'+arg.split('=')[1]
                cls.against_staging = True
                return
        super().setUpClass()
        cls.against_staging = False
        cls.server_url = cls.live_server_url    
       # cls.browser = webdriver.Chrome()
    
       
    @classmethod
    def tearDownClass(cls):
        if not cls.against_staging:
            super().tearDownClass()
       #     cls.browser.quit()
   
    def setUp(self):
            self.browser = webdriver.Chrome()             
            #if 'localhost' in self.server_url:    
            #    self.student = mommy.make('Student', gpa=3.5)
            test_employer = mommy.make('Employer')
            test_employee = mommy.make('Employee', employer=test_employer)
            self.student_computer_science = mommy.make('Student', 
                                                       gpa=3.5, 
                                                       major='Computer Science',
                                                       activities= [mommy.make('Activity')], 
                                                       areas_of_interest= [mommy.make('AreaOfInterest')], 
                                                       competitions= [mommy.make('Competition')],                                                         
                                                       employers = [test_employer], 
                                                       future_plans = [mommy.make('FuturePlan')], 
                                                       hobbies = [mommy.make('Hobby')], 
                                                       magnet_program = mommy.make('MagnetProgram'), 
                                                       accomplishments = [mommy.make('MiscAccomplishment')], 
                                                       projects = [mommy.make('Project')], 
                                                       quotes = [mommy.make('Quote')], 
                                                       reviews = [mommy.make('Review', reviewer=test_employee)], 
                                                       school = mommy.make('School'), 
                                                       tasks = [mommy.make('Task', employer=test_employer)],
                                                       story = 'test story',
                                                       _fill_optional=True
                                                       )
            self.student_mathematics = mommy.make('Student', gpa=4.2, major='Mathematics')
            self.student_psychology = mommy.make('Student', gpa=3.2, major='Psychology')
            #self.user,self.test = mommy.make('newtracker.users.User', make_m2m=True)
            #print(self.student)
           # self.student.save()

    def tearDown(self):
        if self._test_has_failed():
            if not os.path.exists(SCREEN_DUMP_LOCATION):
                os.makedirs(SCREEN_DUMP_LOCATION)
            for ix, handle in enumerate(self.browser.window_handles):
                self._windowid = ix
                self.browser.switch_to_window(handle)
                self.take_screenshot()
                self.dump_html()
        self.browser.quit()
        #return super().tearDown()
    

    @wait
    def wait_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_table')          
        self.assertIn(row_text, table.text)

    @wait
    def check_in_body_text(self, field):        
        self.assertIn(str(field), self.browser.find_element_by_tag_name('body').text)
     
    def check_all_body_text(self, field):
        for entry in field.all():
           self.assertIn(str(entry), self.browser.find_element_by_tag_name('body').text)            
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
    
    

    def _test_has_failed(self):
        # slightly obscure but couldn't find a better way!
        return any(error for (method, error) in self._outcome.errors)

    def take_screenshot(self):
        filename = self._get_filename() + '.png'
        print('screenshotting to', filename)
        self.browser.get_screenshot_as_file(filename)

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print('dumping page HTML to', filename)
        with open(filename, 'w') as f:
            f.write(self.browser.page_source)

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{classname}.{method}-window{windowid}-{timestamp}'.format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )