from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title'] #id,제목 보여주소
    list_display_links = ['title'] #제목에 링크
    search_fields=['title'] #제목으로 검색