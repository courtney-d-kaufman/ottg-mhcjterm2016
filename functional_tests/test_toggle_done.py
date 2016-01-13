from. base import TodoFunctionalTest
from selenium import webdriver

class ToggleDoneTest(TodoFunctionalTest):
    def toggle_todo_done(self, todo_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        for row in rowsL 

    def check_marked_off(self, todo_text):
        pass

    def test_can_toggle_finished_items(self):

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
        self.toggle_todo_done('Buy peacock feathers')
        self.toggle_todo_done('Buy fishing line')

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

        self.toggle_todo_done('Tie some flies')
        self.check_marked_off('Tie some flies')
