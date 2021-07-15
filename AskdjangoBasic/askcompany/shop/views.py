from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, request

def achieve_year(request,year):
    return HttpResponse('{}년도에 대한내용'.format(year))

## 주요request 속성
# request.method: GET,POST 요청인지 알려줌
# request.META: META정보(요청 header포함)
# request.GET,request.POST