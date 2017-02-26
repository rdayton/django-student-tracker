from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class StudentSelectTest(FunctionalTest):

    def test_student_basketball_view_click(self):
        self.browser.get(self.server_url)
        self.get_gpa_input_box().send_keys('3.0'+Keys.ENTER) 
        # She clicks a link to view the students
        self.browser.find_element_by_id('view-'+str(self.student_computer_science.pk)).click()
        # She is sent to a page to select a template
        self.assertIn( 'view',self.browser.current_url)

        self.browser.find_element_by_link_text('Basketball').click()
        self.assertIn( 'basketball',self.browser.current_url)
        self.assertIn(str(self.student_computer_science.pk),self.browser.current_url)              
        self.assertIn(str(self.student_computer_science), self.browser.find_element_by_tag_name('body').text)
        self.assertIn(str(self.student_computer_science.gpa), self.browser.find_element_by_tag_name('body').text)  

    def test_student_clean_view_click(self):
        self.browser.get(self.server_url)
        self.get_gpa_input_box().send_keys('3.0'+Keys.ENTER) 
        # She clicks a link to view the students
        self.browser.find_element_by_id('view-'+str(self.student_computer_science.pk)).click()
        # She is sent to a page to select a template
        self.assertIn( 'view',self.browser.current_url)

        self.browser.find_element_by_link_text('Clean').click()
        self.assertIn( 'clean',self.browser.current_url)
        self.assertIn(str(self.student_computer_science.pk),self.browser.current_url)              
        self.assertIn(str(self.student_computer_science), self.browser.find_element_by_tag_name('body').text)
        self.assertIn(str(self.student_computer_science.gpa), self.browser.find_element_by_tag_name('body').text) 
