from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class SearchValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty search. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('name_input').send_keys('\n')

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Search field can not be blank")
        # She tries again with some text for the item, which now works
        self.browser.find_element_by_id('name_input').send_keys('Bob'+Keys.ENTER)
        
        self.check_for_row_in_table('Bob')
        # Perversely, she now decides to submit a second blank list item
        self.browser.find_element_by_id('name_input').send_keys('\n')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Search field can not be blank")
        # And she can correct it by filling some text in
        self.browser.find_element_by_id('name_input').send_keys('Bob'+Keys.ENTER)
        self.check_for_row_in_table('Bob')