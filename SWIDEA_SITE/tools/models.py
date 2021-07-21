from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=100)
    kind=models.CharField(max_length=100)
    description=models.TextField()
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self): #제목나오게
        return self.title 
    def summary(self): #요약
        return self.content[:50]