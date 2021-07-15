#앱을 생성했을때, 앱내에 urls.py를 생성하기
#from django.urls import path
#from 앱이름 import views

from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views
register_converter(FourDigitYearConverter, 'yyyy')

app_name = "shop"

urlpatterns = [
    path('achieve/<yyyy:year>/', views.achieve_year),
]