from django.conf import settings
from django.urls import path
from . import views

from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('like_ajax/',views.like_ajax,name='like_ajax'),
    path('create_ajax/',views.create_ajax,name='create_ajax'),
    path('delete_ajax/',views.delete_ajax,name='delete_ajax'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)