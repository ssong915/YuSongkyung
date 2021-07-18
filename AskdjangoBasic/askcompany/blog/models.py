from django.conf import settings
from django.db import models
from askcompany.utils import uuid_upload_to

class Post(models.Model):    
    #author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #related_name이름 충돌
    author_name=models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    content=models.TextField()
    photo=models.ImageField(blank=True,upload_to=uuid_upload_to)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # OneToOneField: 한명의 유저는 한명의 필드
#     blog_url = models.URLField(blank=True)

# class Post(models.Model):    
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # ForeignKey(외래키): 다수의 코멘트ok
#     title = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(allow_unicode=True, db_index=True)
#     content = models.TextField(blank=True)
#     image = models.ImageField(blank=True) #Pillow
#     comment_count = models.PositiveIntegerField(default=0) #댓글갯수
#     tag_set = models.ManyToManyField('Tag', blank=True) 
#     #ManyToManyField: 하나의 포스팅은 다수의 태그 가능
#     is_publish = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # ForeignKey: 다수의 코멘트ok
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Tag(models.Model): 
#     name = models.CharField(max_length=50, unique=True)