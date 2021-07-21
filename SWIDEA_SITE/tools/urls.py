from django.contrib import admin
from django.urls import path
from . import views

app_name='tools'

urlpatterns = [
    path('',views.tool_list,name='tool_list'),
    path('create/',views.tool_create,name='tool_create'),
    path('<int:pk>/detail/',views.tool_detail,name='tool_detail'),
    path('<int:pk>/update/',views.tool_update,name='tool_update'),
    path('<int:pk>/delete/',views.tool_delete,name='tool_delete'),
]