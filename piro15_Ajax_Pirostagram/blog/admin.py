from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title'] 
    list_display_links = ['title'] #제목에 링크



@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','post','comment'] 