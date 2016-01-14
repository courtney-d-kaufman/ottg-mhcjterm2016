from .base import TodoFunctionalTest

class ManyListsTests(TodoFunctionalTest):
    def change_list_name(self, list_name):
        pass

    def test_can_create_and_view_multiple_lists(self):
        # Edith comes to the home page, creates a new list,
        # and fills in xyr grocery list.
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('Buy milk')
        self.enter_a_new_item('Buy cheese')
        self.check_for_row_in_list_table('Buy milk')
        self.check_for_row_in_list_table('Buy cheese')

        # Xe sees xe can change a list name
        self.change_list_name('Groceries')

        # Edith goes back to the home page & sees xyr grocery list
        self.browser.get(self.live_server_url)
        self.check_for_row_in_list_table('Groceries')

        # Edith creates a new list for xyr Art History homework
        self.browser.enter_a_new_item('Read Camille')

        # Edith opens the home page later & sees both lists
        self.browser.get(self.live_server_url)
        self.check_for_row_in_list_table('Groceries')
        self.check_for_row_in_list_table('Read Camille')

        # Edith goes to the grocery list and sees what xe needs to buy
        row = find_table_row('Groceries')
        row.find_elements_by_tag_name('a').click()
        self.check_for_row_in_list_table('Buy milk')
        self.check_for_row_in_list_table('Buy cheese')
