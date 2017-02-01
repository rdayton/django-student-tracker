from selenium import webdriver
import unittest
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    def test_can_search(self):
        self.browser.get(self.live_server_url)

        self.assertIn('newtracker', self.browser.title)
        self.fail('Finish the test!')
