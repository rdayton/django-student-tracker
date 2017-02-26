from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class MultiStudentSelectTest(FunctionalTest):

    def test_student_business_view_click(self):
        self.browser.get(self.server_url)
        
        self.get_gpa_input_box().send_keys('3.0'+Keys.ENTER) 

        self.browser.find_element_by_id('check-'+str(self.student_computer_science.pk)).click()
        self.browser.find_element_by_id('check-'+str(self.student_mathematics.pk)).click()
        self.browser.find_element_by_id('multi-submit').click()
        self.assertIn('multi', self.browser.current_url)
        self.browser.find_element_by_link_text('Business').click()
        self.assertIn('business', self.browser.current_url)
        self.assertIn(str(self.student_computer_science), self.browser.find_element_by_tag_name('body').text)