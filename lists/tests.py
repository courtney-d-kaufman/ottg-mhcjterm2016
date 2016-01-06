#from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

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

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()

        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        # key = item_text,  value is a new list item (hashmaps)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
        'home.html', {'new_item_text': 'A new list item'})

        self.assertEqual(response.content.decode(), expected_html)
