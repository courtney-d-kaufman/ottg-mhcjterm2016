from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
    #if request.method == 'POST':
        #Item.objects.create(text=request.POST['item_text'])
        #return redirect('/lists/the-only-list/')
    return render(request, 'home.html')
    # Python first return statement it hits it would evaluate
    # always add new item text to render method
    # pass all the items into the template and render them

def new_list(request):
    new_list = List.objects.create()
    # new_list = List()
    # new_list.save()
    item = Item.objects.create(text=request.POST['item_text'], list=new_list)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        new_list.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error})
    return redirect('/lists/%d/' % (new_list.id,))

# from capture group in url
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    #items = Item.objects.filter(list=list_)
    # python list of type item, list of all the item models where that item's list properties we're looking up
    # items is a key, assert that { 'items': items, } has a property list set to current list, error
    # means that list object not there
    return render(request, 'list.html', { 'list': list_, })

# list ID is captured
def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id))
