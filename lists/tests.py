#from django.test import TestCase
from django.core.urlresolvers import resolve
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

    def test_home_page_returns_correct_html(self):
        # url to look for
        request = HttpRequest()
        # pass into the home page
        response = home_page(request)

        # use assertions on the response
        # a lot of HTML files don't start with HTML
        # these lines could be written less brittly, a space might throw it off
        self.assertTrue(response.content.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith('</html>'))



# Create your tests here.
# write a test to fail, then write a test to pass kata from martial arts
# how many computer scientists does it take to pull down a projection screen?
# Two, apparently

#class SmokeTest(TestCase):
    # tests start with test_
    #def test_bad_maths(self):
        #self.assertEqual(1+1, 3)
