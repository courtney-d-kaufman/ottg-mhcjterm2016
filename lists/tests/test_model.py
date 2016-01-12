# from django.test import TestCase
# from django.core.urlresolvers import resolve
# from django.template.loader import render_to_string
# from django.http import HttpRequest
# from lists.views import home_page
from django.core.exceptions import ValidationError
from django.test import TestCase
from lists.models import Item, List

# cmd / toggles commenting
# grep -E 'class|def' lists/tests.py shows you classes and methods in a file

class ItemAndListModelsTest(TestCase):
    def test_saving_and_retrieving_items_in_list(self):
        new_list = List()
        new_list.save()

        # call constructor as function and returns instance of object, don't need new instance
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        # At this line, what is first_item.list ???
        first_item.list = new_list
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = new_list
        second_item.save()

        # retrieve saved items
        saved_list = List.objects.first()
        self.assertEqual(new_list, saved_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        #check that items line up
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(first_saved_item.list, new_list)
        self.assertEqual(second_saved_item.list, new_list)

    def test_cannot_save_empty_list_items(self):
        new_list = List.objects.create()
        item = Item(list=new_list, text='')

        ## Two ways to write this:
        # try:
        #     item.save()
        #     self.fail('The save should have raised an exception.')
        #     except ValidationError
        #         pass

            #
        with self.assertRaises(ValidationError):
            item.save()
            # This happens in validation instead of save
            item.full_clean()
