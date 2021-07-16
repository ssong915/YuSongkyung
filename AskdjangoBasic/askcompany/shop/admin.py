from django.contrib import admin
from .models import Item

#admin.site.register(Item) #admin페이지에 SHOP-Item 항목 생성
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price','is_publish'] #배열 안에 것들 출력
    list_display_links = ['name'] # name에 링크걸기
    list_filter = ['is_publish','updated_at']
    search_fields = ['name'] # name으로 검색하기

    def short_desc(self, item):
        return item.desc[:20] #desc의 처음 20자만 가져오기