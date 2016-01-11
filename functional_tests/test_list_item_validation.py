from unittest import skip
from .base import TodoFunctionalTest

class ItemValidationTest(TodoFunctionalTest):
    @skip("Haven't implemented this.")
    def test_cannot_add_empty_list_item(self):
        # Edith goes to the home page, and accidentally tries
        # to submit an empty list item.
        # Xe hits "Enter" on the empty input box.

        # The home page refreshes, and there is an error message
        # saying that list items cannot be blank

        # Xe tries again with some text for the item,
        # which now works.

        # Edith perversely tries to enter a second blank item.

        # Xe receives a similar warning on the list page.

        # And xe can correct it by filling some text in.

        self.fail('Finish the test!')
