from selenium import webdriver
import unittest
from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys

class FunctionalTest(StaticLiveServerTestCase):
    
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
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

class NewVisitorTest(FunctionalTest):

    def test_can_search(self):
        self.browser.get(self.server_url)

        self.assertIn('newtracker', self.browser.title)
        self.fail('Finish the test!')

class SearchValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
    # Edith goes to the home page and accidentally tries to submit
    # an empty search. She hits Enter on the empty input box

    # The home page refreshes, and there is an error message saying
    # that list items cannot be blank

    # She tries again with some text for the item, which now works

    # Perversely, she now decides to submit a second blank list item

    # She receives a similar warning on the list page

    # And she can correct it by filling some text in
        self.fail('write me!')