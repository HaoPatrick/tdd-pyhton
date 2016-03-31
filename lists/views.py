from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item
# Create your views here.

def home_page(request):
    if request.method=='POST':
        item_text=request.POST['item_text']
        Item.objects.create(text=item_text)
        return redirect('/list/the-only-list-in-the-world/')
    return render(request,'home.html')
    #return render(request,'home.html')

def view_list(request):
    items=Item.objects.all()
    return render(request,'list.html',{'new_item_text':items})
