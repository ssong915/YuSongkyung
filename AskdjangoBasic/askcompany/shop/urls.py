#앱을 생성했을때, 앱내에 urls.py를 생성하기
#from django.urls import path
#from 앱이름 import views

from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views
register_converter(FourDigitYearConverter, 'yyyy')

app_name = "shop"

urlpatterns = [
    #path('item/',item_list,name="item_list") -> item/주소랑 매칭이되면, item_list 함수를 호출, 이 이름은 "item_list"
    path('achieve/<yyyy:year>/',views.achieve_year),
    path('',views.item_list),
    path("<int:pk>/", views.item_detail),
]