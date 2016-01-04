from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home_page = None
# raise Resolver404({'tried': tried, 'path': new_path})
# Resolver404: {u'path': u'', u'tried': [[<RegexURLResolver <RegexURLPattern list> (admin:admin) ^admin/>]]}
# we didn't define this route

# AttributeError: 'NoneType' object has no attribute 'content'
def home_page(request):
    # first add request because needs param
    # pass
    # self.assertTrue(response.content.startswith('<html>'))
    # AssertionError: False is not true

    return HttpResponse('<html><title>To-Do lists</title></html>')
