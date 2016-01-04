#from django.test import TestCase
from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# it's better to fail in a way we know will happen then to fail in an unexpected way
# test first before anything else

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # matches everything after the domain name
        # app.io/(123ABC) this portion
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        # ImportError: cannot import name home_page

# Create your tests here.
# write a test to fail, then write a test to pass kata from martial arts
# how many computer scientists does it take to pull down a projection screen?
# Two, apparently

#class SmokeTest(TestCase):
    # tests start with test_
    #def test_bad_maths(self):
        #self.assertEqual(1+1, 3)
