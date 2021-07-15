from django.db import models

class Item(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True) #blank=True: 빈칸도 허용함 (default: False)
    price=models.PositiveIntegerField() #양수 받아오기

    created_at=models.DateTimeField(auto_now_add=True) #날짜+시간 #첨 추가
    updated_at=models.DateTimeField(auto_now=True) #업데이트될때 추가


