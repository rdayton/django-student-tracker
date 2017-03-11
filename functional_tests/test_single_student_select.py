from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class SingleStudentSelectTest(FunctionalTest):

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

        self.browser.find_element_by_id("edit-story-"+str(self.student_computer_science.pk)).click()
        new_story_text = "new story"
        self.browser.execute_script("tinyMCE.activeEditor.setContent('%s')" % new_story_text)

        # # used to get around save button visibility issue with selenium
        self.browser.execute_script("document.querySelector('#save-story').click()")

        self.check_in_body_text(new_story_text)
        

   # @skip('testing other')
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
     
   # @skip('testing other')
    def test_student_plain_view_click(self):
        self.browser.get(self.server_url)
        self.get_gpa_input_box().send_keys('3.0'+Keys.ENTER) 
        # She clicks a link to view the students
        self.browser.find_element_by_id('view-'+str(self.student_computer_science.pk)).click()
        # She is sent to a page to select a template
        self.assertIn( 'view',self.browser.current_url)

        self.browser.find_element_by_link_text('Plain').click()
        self.assertIn( 'plain',self.browser.current_url)
        self.assertIn(str(self.student_computer_science.pk),self.browser.current_url)              
        self.check_in_body_text(self.student_computer_science)
        self.check_in_body_text(self.student_computer_science.school)       
        self.check_in_body_text(self.student_computer_science.story)    
        self.check_in_body_text(self.student_computer_science.gpa)
        self.check_in_body_text(self.student_computer_science.student_id)
        self.check_in_body_text(self.student_computer_science.magnet_program) 
        self.check_all_body_text(self.student_computer_science.projects)         
        self.check_all_body_text(self.student_computer_science.activities) 
        self.check_all_body_text(self.student_computer_science.hobbies)  
        self.check_all_body_text(self.student_computer_science.quotes)  
        self.check_all_body_text(self.student_computer_science.competitions)
        self.check_all_body_text(self.student_computer_science.accomplishments)  
        self.check_all_body_text(self.student_computer_science.areas_of_interest)  
        self.check_all_body_text(self.student_computer_science.future_plans)
        self.check_all_body_text(self.student_computer_science.employers) 
        self.check_all_body_text(self.student_computer_science.reviews)  
        self.check_all_body_text(self.student_computer_science.tasks) 