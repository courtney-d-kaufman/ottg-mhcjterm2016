# hit tab twice to correctly indent everything we have below
# shift tab to undo
#from django.test import LiveServerTestCase
from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# automatically run a web browser
from selenium import webdriver
# see keys you can import
from selenium.webdriver.common.keys import Keys
# now make it a unit test
# import unittest

# nice test oriented things, cleanly, efficiently, pragmatically
class TodoFunctionalTest(StaticLiveServerTestCase):
    # self is equivalent to this
    def setUp(self):
        # create a new instance of the browser at the beginning
        self.browser = webdriver.Firefox()
        # if something goes wrong in three seconds, then go ahead and fail
        # Selenium says something is wrong, crash it 3 seconds is very generous
        # good for web driver test cases
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # and close it at the end
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def enter_a_new_item (self, todo_text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(todo_text)
        inputbox.send_keys(Keys.ENTER)
