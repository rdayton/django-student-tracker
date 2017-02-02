from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(FunctionalTest):

    def test_can_search(self):
        self.browser.get(self.server_url)

        self.assertIn('newtracker', self.browser.title)
        
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('name_input')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Search'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Bob')

        # When she hits enter, the page updates, and now the page lists
        # the name she was searching for
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_table('Bob')
        
        

