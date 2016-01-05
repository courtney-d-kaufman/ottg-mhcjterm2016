# git log -- lists what you've done before

# hit tab twice to correctly indent everything we have below
# shift tab to undo

# automatically run a web browser
from selenium import webdriver
# see keys you can import
from selenium.webdriver.common.keys import Keys
# now make it a unit test
import unittest

class NewVisitorTest(unittest.TestCase):
# nice test oriented things, cleanly, efficiently, pragmatically

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

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has head about a cool new online to-do app.
        # (Feel free to use non-cisgender pronouns, the book uses she)
        # Xe goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # Xe notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        # find the first H1 tag, assume it's the one you want and look for text To-Do
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Xe is invited to enter a to-do item straight away
        # New input box as well as instruction
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
        inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # Xe types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When xe hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
        # quick and dirty, but will later prove to be a bad decision
            any(row.text == '1. Buy peacock feathers' for row in rows)
        )

        self.assertIn('To-Do', self.browser.title)

#def test_can_log_into_a_new_account(self):

# assert 'To-Do' in browser.title


# There is still a text book inviting xyr to add another item.
# Xe enters 'Use peacock feathers to make fly'
# (Edith is very methodical)

# The homepage updates again, and now shows both items on xyr list,

# Edith wonders whether the site with remember xyr list. Then xe sees
# That the site has generated a unique url for xyr -- there is some
# explanatory text to that effect.

# Xe visites that url -- xyr to-do list is still there.

# Satisfied, xe goes back to sleep

#browser.quit()
        # we're not done until we're actually done
        self.fail('Finish the app!')

    #use the unittest main, and ignore all warnings
if __name__ == '__main__':
    unittest.main()

# unittest.main(warnings ='ignore')


# Nothing in software has ever been intuitive

# Test for false
# if ! 'Django' in browser.title:
    # throw new AssertionError

# git allows us to keep revision history, source control is that on steroids
# git is source control program
# git -V or git -- version


# git status -- what's going on with project that git cares about
# initial commit -- haven't made any changes yet
# git add -- tell git we care about these files git add .
# git commit -- save changes
# .pyc is a compiled python file, binary, don't want in source control, they're generated
# echo '*.pyc' >> .gitignore -- git creates a file to ignore .pyc files every time


# browser = webdriver.Firefox()
# port 8000, where it is going to be, start a server on port 8000
# browser.get('http://localhost:8000')

# write the assertion (test) before writing the program
# we can't find Django because there isn't anything there in the first place
# http://127.0.0.1:8000/

# built in construct in python, does that string (Django)
# show up anywhere in that variable (browser, reference to something that managaes firefox browser window)
# .title (the label on the tab in web browser)
# assert -- does this resolve to true, if so assert goes on its merry way, otherwise throws a new execption
# assert 'Django' in browser.title
