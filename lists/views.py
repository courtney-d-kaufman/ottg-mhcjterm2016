from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# home_page = None
# raise Resolver404({'tried': tried, 'path': new_path})
# Resolver404: {u'path': u'', u'tried': [[<RegexURLResolver <RegexURLPattern list> (admin:admin) ^admin/>]]}
# we didn't define this route

# AttributeError: 'NoneType' object has no attribute 'content'
def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', '')
    })

    # first add request because needs param
    # pass
    # self.assertTrue(response.content.startswith('<html>'))
    # AssertionError: False is not true

    # render -- takes a function and a path inside of templates and gives you the HTML back
    # that file name is inside the templates folder

    # TemplateDoesNotExist: home.html

    # return HttpResponse('<html><title>To-Do lists</title></html>')
