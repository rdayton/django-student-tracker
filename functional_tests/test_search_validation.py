from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from unittest import skip


class SearchValidationTest(FunctionalTest):
    
   
    def test_cannot_add_empty_field_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty search. She hits Enter on the empty input box
        self.browser.get(self.server_url)

        self.get_gpa_input_box().send_keys('\n')

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_gpa:invalid'))
        # She tries again with some text for the item, which now works
        self.get_gpa_input_box().send_keys('3.0'+Keys.ENTER)    
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_gpa:valid'))    
        self.wait_for_row_in_table(self.student_computer_science.user.username)
        
        # Perversely, she now decides to submit a second blank list item
        self.get_gpa_input_box().send_keys(Keys.ENTER)
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_gpa:invalid'))
        
       
    def test_proper_columns_displayed(self):
        self.browser.get(self.server_url)

        self.get_gpa_input_box().send_keys('0.1'+Keys.ENTER)
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_gpa:valid'))
        table = self.browser.find_element_by_id('id_table')
        
        self.wait_for(lambda: self.assertIn('GPA', table.text))
        #self.assertIn('4.0', table.text)
        #self.assertIn('School', table.text)
        #self.assertIn('Major', table.text)
        
    
    def test_string_in_gpa_field(self):
        self.browser.get(self.server_url)
        # And she then accidentally enters a username
        self.get_gpa_input_box().send_keys('bob'+Keys.ENTER)        
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_gpa:invalid'))
    
        #TODO:expand later