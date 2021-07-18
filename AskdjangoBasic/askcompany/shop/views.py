from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, request
from .models import Item
import re
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


def item_new(request, item=None):
    error_list = []
    initial = {}

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        name = data.get('name')
        desc = data.get('desc')
        price = data.get('price')
        photo = files.get('photo')
        is_published = data.get('is_published') in (True, 't', 'True', '1')

        # 유효성 검사
        if len(name) < 5:
            error_list.append('name을 5글자 이상 입력해주세요.')

        if re.match(r'^[\da-zA-Z\s]+$', desc):
            error_list.append('한글을 입력해주세요.')

        if not error_list:
            # 저장 시도
            if item is None:
                item = Item()

            item.name = name
            item.desc = desc
            item.price = price
            item.is_published = is_published

            if photo:
                item.photo.save(photo.name, photo, save=False)

            try:
                item.save()
            except Exception as e:
                error_list.append(e)
            else:
                return redirect(item)  # item.get_absolute_url()이 호출됨.

        initial = {
            'name': name,
            'desc': desc,
            'price': price,
            'photo': photo,
            'is_published': is_published,
        }
    else:
        if item is not None:
            initial = {
                'name': item.name,
                'desc': item.desc,
                'price': item.price,
                'photo': item.photo,
                #'is_published': item.is_published,
            }

    return render(request, 'shop/item_form.html', {
        'error_list': error_list,
        'initial': initial,
    })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)



