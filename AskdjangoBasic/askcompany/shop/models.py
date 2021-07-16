from django.db import models
class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True) #blank=True: 빈칸도 허용함 (default: False)
    price = models.PositiveIntegerField(default="") #양수 받아오기
    is_publish = models.BooleanField(default=False) #날짜+시간 #첨 추가
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) #업데이트될때 추가

    def __str__(self):
        # return self.name
        # return '<{}> {}'.format(self.pk, self.name)
        return f'<{self.pk}> {self.name}'
