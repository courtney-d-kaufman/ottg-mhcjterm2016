# hit tab twice to correctly indent everything we have below
# shift tab to undo
#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# automatically run a web browser
from selenium import webdriver
# see keys you can import
from selenium.webdriver.common.keys import Keys
# now make it a unit test
# import unittest

# nice test oriented things, cleanly, efficiently, pragmatically
class NewVisitorTest(StaticLiveServerTestCase):

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

    #def send_keys (self, keys):
        #inputbox = self.browser.find_element_by_id('id_new_item')
        #inputbox.send_keys(keys)
        #inputbox.send_keys(Keys.ENTER)

    def enter_a_new_item (self, todo_text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(todo_text)
        inputbox.send_keys(Keys.ENTER)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has head about a cool new online to-do app.
        # (Feel free to use non-cisgender pronouns, the book uses she)
        # Xe goes to check out its homepage
        #self.browser.get('http://localhost:8000')
        #self.brower.set_window_size(1024, 768)
        #self.browser.get(self.live_server_url)

        # Xe is invited to enter a to-do item straight away
        # New input box as well as instruction
        # Xe notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        # find the first H1 tag, assume it's the one you want and look for text To-Do
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #self.assertEqual(
        #inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        #)

        # Xe types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        self.enter_a_new_item('Buy peacock feathers')

        # When xe hits enter, she is taken to a new URL, and now the page lists
        # "1. Buy peacock feathers"
        # as an item in a to-do lists
        edith_list_url = self.browser.current_url
        self.assertRegexpMatches(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1. Buy peacock feathers')

        # There is still a text book inviting xyr to add another item.
        # Xe enters 'Use peacock feathers to make fly'
        # (Edith is very methodical)
        self.enter_a_new_item('Use peacock feathers to make fly')

        # The homepage updates again, and now shows both items on xyr list
        table = self.browser.find_element_by_id('id_list_table')
        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table('2. Use peacock feathers to make fly')

        # Edith wonders whether the site with remember xyr list. Then xe sees
        # That the site has generated a unique url for xyr -- there is some
        # explanatory text to that effect.

        #self.assertIn('To-Do', self.browser.title)

        # Xe visites that url -- xyr to-do list is still there.

        # Satisfied, xe goes back to sleep
        # we're not done until we're actually done
        # self.fail('Finish the app!')

        # Now a new user, Francis, comes along.

        ## We use a new browser session to make sure no information
        # My 101 professor dropped me on my head one time
        ## of Edith's comes along (EG cookies, localStorage)
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's list.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item.
        # neutering nentering
        # They are less interesting than Edith.
        self.enter_a_new_item('Buy milk')

        # Francis gets their own URL
        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual (francis_list_url, edith_list_url)

        #There is still no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satsified, they both go back to sleep.

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.set_window_size(1024, 768)
        self.browser.get(self.live_server_url)

        # She notices the input box is nicely centered
        self.check_input_box_is_centered()

        # She starts a new list and sees the box is centered.
        self.enter_a_new_item('testing')
        self.check_input_box_is_centered()

    def check_input_box_is_centered(self):
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + (inputbox.size['width'] / 2),
            # accounts for rounding errors according to browser
            512,
            delta=5
        )




#use the unittest main, and ignore all warnings
#if __name__ == '__main__':
    #unittest.main()
