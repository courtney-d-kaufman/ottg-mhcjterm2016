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

class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        # other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/add_item' % (correct_list.id,),
            data={'item_text': 'A new item for an existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        # other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            '/lists/%d/add_item' % (correct_list.id,),
            data={'item_text': 'A new item for an existing list'}
        )

        self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))

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
