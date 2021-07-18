from django.db import models
from django.conf import settings
from askcompany.utils import uuid_upload_to
from django.urls import reverse
class Item(models.Model):
    name = models.CharField(max_length=100) #validators로 최소길이라던지 여러 제한을 놓을 수 있음
    desc = models.TextField(blank=True) #blank=True: 빈칸도 허용함 (default: False)
    price = models.PositiveIntegerField(default="") #양수 받아오기
    photo=models.ImageField(blank=True,upload_to=uuid_upload_to)
    is_publish = models.BooleanField(default=False) #날짜+시간 #첨 추가
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) #업데이트될때 추가

    def __str__(self):
        # return self.name
        # return '<{}> {}'.format(self.pk, self.name)
        return f'<{self.pk}> {self.name}'

    def get_absolute_url(self):
        return reverse('shop:item_detail',args=[self.pk])

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #related_name이름 충돌

# < ForeignKey > 
# (1) 1:N 중 N에다가 foreignkey명시
# class Post(models.Model): # 1
#     title = models.CharField(max_length=100)
#     content = models.TextField()
# class Comment(models.Model): # N
#     post = models.ForeignKey(Post, on_delete=models.CASCADE) # ForeignKey(to, on_delete: 삭제시 Rule)
#     message = models.TextField()
# (2) related_name
# (3) ForeignKey.limit_choices_to 옵션

# < OneToOneField >
# (1) 1:1 어디든 상관X
# class User(AbstractBaseUser):
# class Profile(models.Model):
#   author = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

# < ManyToManyField >
# (1) M:N 어디든 상관X
# (2) ManyToManyField(to,blank=False) ==> blank 태그 중요!!!
# 방법 1)
# class Post(models.Model):
#   tag_set = models.ManyToManyField('Tag', blank=True)
# class Article(models.Model):
#   tag_set = models.ManyToManyField('Tag', blank=True)
# class Tag(models.Model):
#   name = models.CharField(max_length=100, unique=True)
# 방법 2) 🙆‍♂️
# class Post(models.Model):
# ...
# class Article(models.Model):
# ...
# class Tag(models.Model):
#    name = models.CharField(max_length=100, unique=True)
#    post_set = models.ManyToManyField('Post', blank=True)
#    article_set = models.ManyToManyField('Article', blank=True)
