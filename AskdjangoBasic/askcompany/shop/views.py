from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def achieve_year(request,year):
    return HttpResponse('{}년도에 대한내용'.format(year))
