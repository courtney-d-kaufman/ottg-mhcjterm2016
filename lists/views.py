from django.shortcuts import render, redirect
from lists.models import Item

def home_page(request):
    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()
    # control flow can get to here if it doesn't evaluate first branch of if statement
    if request.method == 'POST':
        #new_item_text = request.POST['item_text']
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list/')
    return render(request, 'home.html')
    #else:
        #new_item_text = ''
    # Python first return statement it hits it would evaluate
    # always add new item text to render method
    # pass all the items into the template and render them

def view_list(request):
    items = Item.objects.all()
    print "in view list"
    return render(request, 'list.html', { 'items': items, })


# commas at the end of the line, oxford comma equivalent because you don't have to
# add it later
