from. base import TodoFunctionalTest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class ToggleDoneTest(TodoFunctionalTest):
    def toggle_todo_done(self, todo_text_list):
        for todo_text in todo_text_list:
            row = self.find_table_row(todo_text)
            row.find_element_by_tag_name('input').click()
        # If you've ever spent more than ten minutes debugging the same issue, take a break
        self.browser.find_element_by_id('toggle_done').click()

    def check_marked_off(self, todo_text):
        row = self.find_table_row(todo_text)
        try:
            row.find_element_by_css_selector('.todo-done')
        except NoSuchElementException:
            self.fail("%s not marked done!" % (todo_text))

    def check_not_marked_off(self, todo_text):
        try:
            self.check_marked_off(todo_text)
        except:
            return
        self.fail("'%s' is marked done!" % (todo_text))

    def test_can_mark_finished_items(self):

        # Edith makes a quick shopping list
        # Noticing a checkbox to toggle done items.
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('Buy peacock feathers')
        self.enter_a_new_item('Buy fishing line')

        checkbox_selector = 'input[type="checkbox"]'
        checkboxes = self.browser.find_elements_by_css_selector(checkbox_selector)
        self.assertEqual(len(checkboxes), 2)

        # At the store, Edith puts feathers in xyr cart
        # and marks them done on the todo list.
        self.toggle_todo_done([
        'Buy peacock feathers',
        'Buy fishing line'
        ])
        self.check_marked_off('Buy peacock feathers')
        self.check_marked_off('Buy fishing line')

        #self.toggle_todo_done('Buy fishing line')

        # Edith returns home, re-opens xyr todo list,
        # And sees that xyr shopping list is still marked
        # and crossed off.
        current_list_url = self.browser.current_url
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(current_list_url)
        self.check_marked_off('Buy peacock feathers')
        self.check_marked_off('Buy fishing line')

        # Xe adds a note to tie her flies
        # and marks them as done after a nice afternoon of tying.
        self.enter_a_new_item('Tie some flies')
        self.check_marked_off('Buy peacock feathers')
        self.check_marked_off('Buy fishing line')

        self.toggle_todo_done(['Tie some flies'])
        self.check_marked_off('Tie some flies')

    def test_can_toggle_finished_items(self):
        # Edith's fly tying (ties flying) hobby is booming, and xe wants
        # a list that xe can use over and over
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('Buy feathers')
        self.enter_a_new_item('Buy fishing line')
        self.enter_a_new_item('Buy sparkles')

        # Xe looks in xyr closer and already has fishing line.
        self.toggle_todo_done(['Buy fishing line'])
        self.check_marked_off('Buy fishing line')

        # Xe goes to the store, and finishes shopping
        self.toggle_todo_done([
            'Buy feathers',
            'Buy sparkles'
        ])
        self.check_marked_off('Buy feathers')
        self.check_marked_off('Buy fishing line')
        self.check_marked_off('Buy sparkles')

        # Xe makes some flys, and xyr closet is empty
        self.toggle_todo_done([
            'Buy feathers',
            'Buy fishing line',
            'Buy sparkles'
        ])

        self.check_not_marked_off('Buy feathers')
        self.check_not_marked_off('Buy fishing line')
        self.check_not_marked_off('Buy sparkles')
