from .base import FunctionalTest
from selenium import webdriver

class NewVisitorTest(FunctionalTest):

    def test_can_search(self):
        self.browser.get(self.server_url)

        self.assertIn('newtracker', self.browser.title)

