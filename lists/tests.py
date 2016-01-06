#from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item

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

    # test is too long, 20 lines of code and testing multiple things
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()

        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        # 302 -- go somewhere else, 404 not found
        # https://http.cat/ cat photos that tell you what error code means
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        # key = item_text,  value is a new list item (hashmaps)
        #self.assertIn('A new list item', response.content.decode())
        #expected_html = render_to_string(
        #'home.html', {'new_item_text': 'A new list item'})

        #self.assertEqual(response.content.decode(), expected_html)


        # normal get request, don't save any items
        # we're doing a unit of work, not a bunch of work
        # by simply changing the method name we made it a lot more clear what we're going to do

        # test is too long, 20 lines of code and testing multiple things
    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

    def test_home_page_displays_all_items(self):
        Item.objects.create(text='itemy 1')
        Item.objects.create(text='itemy 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('itemy 1', response.content.decode())
        self.assertIn('itemy 2', response.content.decode())


    def test_home_page_doesnt_save_on_GET_request(self):
        # same first line each time
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)

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
