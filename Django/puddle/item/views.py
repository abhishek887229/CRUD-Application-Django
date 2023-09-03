from django.shortcuts import render,get_object_or_404
from .models import Item

def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(is_sold=False)
    return render(request,'item/detail.html',{
                      'item':item,
                      'related_item':related_items,
                  }) 