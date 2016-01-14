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


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item (text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
        except ValidationError:
            error = "You can't have an empty list item"
        #Item.objects.create(text=request.POST['item_text'], list=list_)
        #return redirect('/lists/%d/' % (list_.id,))

    return render(
        request, 'list.html',
        { 'list': list_, 'error': error}
    )

def edit_list(request, list_id):
    list_ = List.objects.get(id=list_id)

    for item in list_.item_set.all():
        item.is_done = False
        item.save()

    # we want a list here, not a single value
    item_ids = request.POST.getlist('mark_item_done')
    for item_id in item_ids:
        item = Item.objects.get(id=item_id)
        item.is_done = True
        item.save()

    return redirect('/lists/%d/' % (list_.id))
