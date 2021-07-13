from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    # 루트 URL
    path('', views.post_list, name='post_list'),
]