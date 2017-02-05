from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time
class NewVisitorTest(FunctionalTest):

    
    def test_can_search(self):
        self.browser.get(self.server_url)

        self.assertIn('newtracker', self.browser.title)
        
        # She is invited to enter a GPA right away
        inputbox = self.browser.find_element_by_id('gpa_input')        

        # She wants to find students with over a 3.0 gpa
        inputbox.send_keys('3.0')

        # When she hits enter, the page updates, and now the page lists
        # the name she was searching for
        inputbox.send_keys(Keys.ENTER)       
        time.sleep(3)
        self.check_for_row_in_table(self.student.user.username)
        
        

