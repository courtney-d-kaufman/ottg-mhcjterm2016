#from django.test import TestCase
from django.core.urlresolvers import resolve
from django.utils.html import escape
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item, List

# cmd / toggles commenting
# grep -E 'class|def' lists/tests.py shows you classes and methods in a file

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_has_todo_lists(self):
        list1 = List.objects.create(name="List 1")
        list2 = List.objects.create(name="List 2")
        response = self.client.get('/')

        context = response.context['todo_lists']
        self.assertEqual(len(context), 2)
        self.assertEqual(context[0], list1)
        self.assertEqual(context[1], list2)

class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
        # no trailing slash, convention is that trailing slash is geting data,
        # no trailing slash is sending data
        '/lists/new',
        data = {'item_text': 'A new list item'}
        )

        #response = home_page(request) -- never actually used, only to evaluate express which self.client.post does
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new',
            data ={'item_text': 'A new lists item'}
        )
        # expects to be able to turn the redirect into an integer
        new_list = List.objects.first()
        self.assertRedirects(response, '/lists/%d/' % (new_list.id,))
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], '/lists/the-only-list/')

    def test_validation_errors_are_sent_back_to_home_page(self):
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        # print(response.content.decode())
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)

    def test_invalid_items_arent_saved(self):
        self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)

    def test_new_list_has_name_of_first_item(self):
        response = self.client.post(
            '/lists/new',
            data ={'item_text': 'A new lists item'}
        )
        
        new_list = List.objects.first()
        self.assertEqual(new_list.name, 'A new lists item')

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        new_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (new_list.id,))
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_lists(self):
        new_list = List.objects.create()
        Item.objects.create(text='itemy 1', list=new_list)
        Item.objects.create(text='itemy 2', list=new_list)

        other_list = List.objects.create()
        Item.objects.create(text='other item 1', list=other_list)
        Item.objects.create(text='other item 2', list=other_list)

        response = self.client.get('/lists/%d/' % (new_list.id,))

        self.assertIn('itemy 1', response.content.decode())
        self.assertIn('itemy 2', response.content.decode())

        self.assertContains(response, 'itemy 1')
        self.assertContains(response, 'itemy 2')
        self.assertNotContains(response, 'other item 1')
        self.assertNotContains(response, 'other item 2')

    def test_passes_correct_list_to_template(self):
        # other_list = List.objects.create()
        # response keeps track of what data used for rendering
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)

    def test_can_save_a_POST_request_to_an_existing_list(self):
        # other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'item_text': 'A new item for an existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_validation_errors_stay_on_list_page(self):
        current_list  = List.objects.create()
        response = self.client.post(
            '/lists/%d/' % (current_list.id,),
            data={'item_text': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)

    def test_invalid_items_arent_saved(self):
        current_list  = List.objects.create()
        self.client.post(
            '/lists/%d/' % (current_list.id),
            data={'item_text': ''}
        )
        self.assertEqual(Item.objects.count(), 0)

    def test_list_view_displays_checkbox(self):
      current_list = List.objects.create()
      Item.objects.create(text="Item 1", list=current_list)
      Item.objects.create(text="Item 2", list=current_list)

      response = self.client.get('/lists/%d/' % (current_list.id,))

      self.assertContains(response, 'input type="checkbox"')

    def test_edit_list_name(self):
        current_list = List.objects.create()
        self.client.post(
            '/lists/%d/' % (current_list.id,),
            data={'list_name': 'New List'}
        )

        self.assertEqual(List.objects.first().name, 'New List')

class EditListTest(TestCase):

    def test_POST_one_item_marks_done(self):
         # Create list and items
         current_list = List.objects.create()
         item1 = Item.objects.create(text="Item 1", list=current_list)
         item2 = Item.objects.create(text="Item 2", list=current_list)

         # POST data
         response = self.client.post(
            '/lists/%d/items/' % (current_list.id,),
            data={'mark_item_done': item1.id}
         )

         # - including toggle item
         self.assertRedirects(response, '/lists/%d/' % current_list.id)

         # Check item is updated
         item1 = Item.objects.get(id=item1.id)
         item2 = Item.objects.get(id=item2.id)
         self.assertTrue(item1.is_done)
         self.assertFalse(item2.is_done)

    def test_POST_multiple_items_done(self):
        current_list = List.objects.create()
        item1 = Item.objects.create(text="Item 1", list=current_list)
        item2 = Item.objects.create(text="Item 2", list=current_list)

        response = self.client.post(
            '/lists/%d/items/' % (current_list.id),
            data={'mark_item_done': [item1.id, item2.id]}
            )

        item1 = Item.objects.get(id=item1.id)
        item2 = Item.objects.get(id=item2.id)
        self.assertTrue(item1.is_done)
        self.assertTrue(item2.is_done)

    def test_POST_zero_items_done(self):
        current_list = List.objects.create()
        item1 = Item.objects.create(text="Item 1", list=current_list)
        item2 = Item.objects.create(text="Item 2", list=current_list)

        response = self.client.post(
            '/lists/%d/items/' % (current_list.id),
            data={ }
            )

        item1 = Item.objects.get(id=item1.id)
        item2 = Item.objects.get(id=item2.id)
        self.assertFalse(item1.is_done)
        self.assertFalse(item2.is_done)

    def test_POST_item_toggles_done(self):
         # Create list and items
         current_list = List.objects.create()
         item1 = Item.objects.create(
            text="Item 1",
            list=current_list,
            is_done=True
         )

         item2 = Item.objects.create(
            text="Item 2",
            list=current_list,
            is_done=False
         )
         # sending state is easier, stick with tools we have
         # POST data
         response = self.client.post(
            '/lists/%d/items/' % (current_list.id,),
            data={'mark_item_done': [item2.id]}
         )

         # - including toggle item
         self.assertRedirects(response, '/lists/%d/' % current_list.id)

         # Check item is updated
         item1 = Item.objects.get(id=item1.id)
         item2 = Item.objects.get(id=item2.id)
         self.assertFalse(item1.is_done)
         self.assertTrue(item2.is_done)
