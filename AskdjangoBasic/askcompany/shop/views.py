from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, request
from django.views.generic import CreateView, UpdateView
from .models import Item
import re
from .forms import ItemForm
## 주요request 속성
# request.method: GET,POST 요청인지 알려줌
# request.META: META정보(요청 header포함)
# request.GET,request.POST

#DB 추가:insert, 수정:update , 삭제:delete

def achieve_year(request,year):
    return HttpResponse('{}년도에 대한내용'.format(year))

def item_list(request):
    qs=Item.objects.all()
    
    return render(request,'shop/item_list.html',{
        'item_list':qs,
    })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, "shop/item_detail.html", {"item": item}) 


# def item_new(request, item=None):
#     if request.method=='POST':
#         form=ItemForm(request.POST,request.FILES,instance=item)
#         if form.is_valid():
#             item=form.save()
#             return redirect(item)
#     else:
#         form=ItemForm(instance=item)

#     return render(request, 'shop/item_form.html', {
#         'form':form,
#     })
# =======>
item_new = CreateView.as_view(model=Item, form_class=ItemForm)


# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)
# ======>

item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)


