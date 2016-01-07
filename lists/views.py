from django.shortcuts import render, redirect
from lists.models import Item

def home_page(request):
    #if request.method == 'POST':
        #Item.objects.create(text=request.POST['item_text'])
        #return redirect('/lists/the-only-list/')
    return render(request, 'home.html')
    # Python first return statement it hits it would evaluate
    # always add new item text to render method
    # pass all the items into the template and render them

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', { 'items': items, })

#def foo(request):
    #return render(request, 'foo.html')

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list/')

# commas at the end of the line, oxford comma equivalent because you don't have to
# add it later
