from django.shortcuts import render, get_object_or_404
from .models import Item

def item_list(request):
    items = Item.published.all()
    return render(request, 'blog/item/list.html', {'items': items})

def item_detail(request, year, month, day, post):
    item = get_object_or_404(Post, slug=post, status='published',publish__year=year,
                        publish__month=month,publish__day=day)
    return render(request,'blog/item/detail.html',{'item': item})
    