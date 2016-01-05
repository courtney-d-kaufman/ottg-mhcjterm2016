#from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest


# it's better to fail in a way we know will happen then to fail in an unexpected way
# test first before anything else
# always concerned with good enough for now in TDD
# always feel free to run your tests even if I haven't yet

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

        # use assertions on the response
        # a lot of HTML files don't start with HTML
        # these lines could be written less brittly, a space might throw it off
        # self.assertTrue(response.content.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', response.content)
        #self.assertTrue(response.content.endswith('</html>'))
        # self.assertTrue(response.content.strip().endswith('</html>'))

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


    #python manage.py for unit tests, can only work on unit test or implementation at a time

# Create your tests here.
# write a test to fail, then write a test to pass kata from martial arts
# how many computer scientists does it take to pull down a projection screen?
# Two, apparently

#class SmokeTest(TestCase):
    # tests start with test_
    #def test_bad_maths(self):
        #self.assertEqual(1+1, 3)
