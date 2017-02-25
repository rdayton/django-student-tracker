from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time
from django.contrib import auth
class NewVisitorTest(FunctionalTest):

    
    def test_can_search(self):
        self.browser.get(self.server_url)        
        '''
        # She is asked to login
        self.assertIn('login', self.browser.current_url)

        # She enters her information
        username_input = self.wait_for(lambda: self.browser.find_element_by_id('id_login'))
        username_input.send_keys('Edith')
        password_input = self.wait_for(lambda: self.browser.find_element_by_id('id_password'))
        password_input.send_keys('Edith')
        password_input.send_keys(Keys.ENTER)   
        '''

        #She is then sent back to the home page
        self.assertIn('newtracker', self.browser.title)
        self.assertIn('login', self.browser.current_url)
        # She is invited to enter a GPA right away
        inputbox = self.get_gpa_input_box()        

        # She wants to find students with over a 3.0 gpa
        inputbox.send_keys('3.0')
        
        # When she hits enter, the page updates, and now the page lists
        # the name she was searching for
        inputbox.send_keys(Keys.ENTER)     
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_gpa:valid'))
        self.wait_for_row_in_table(self.student.user.username)
        
        

