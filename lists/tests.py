#from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item

# cmd / toggles commenting
# grep -E 'class|def' lists/tests.py shows you classes and methods in a file

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # matches everything after the domain name
        # app.io/(123ABC) this portion
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        # ImportError: cannot import name home_page

    # refactoring -- specifically editing code so we maintain the old
    # behavior, but uses different steps to do it
    # it does the same thing but the code is cleaner and more efficient
    def test_home_page_returns_correct_html(self):
        # url to look for
        # first render we've done
        request = HttpRequest()
        # pass into the home page
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

class NewListTest(TestCase):


    # test is too long, 20 lines of code and testing multiple things
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
        self.assertRedirects(response, '/lists/the-only-list/')
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], '/lists/the-only-list/')

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        Item.objects.create(text='itemy 1')
        Item.objects.create(text='itemy 2')

        response = self.client.get('/lists/the-only-list/')

        self.assertIn('itemy 1', response.content.decode())
        self.assertIn('itemy 2', response.content.decode())

    #def test_home_page_doesnt_save_on_GET_request(self):
        # same first line each time
        #request = HttpRequest()
        #home_page(request)
        #self.assertEqual(Item.objects.count(), 0)

# class FooTest(TestCase):
#     def test_foo_resolve(self):
#         found = resolve('/foo/')
#         self.assertEqual(found.func, foo)
#
#     def test_uses_foo_template(self):
#         response = self.client.get('/foo/')
#         self.assertTemplateUsed(response, 'foo.html')

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        # call constructor as function and returns instance of object, don't need new instance
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        # retrieve saved items
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        #check that items line up
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
