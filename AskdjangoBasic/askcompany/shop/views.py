from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, request
from .models import Item
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


