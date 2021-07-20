from django.db import models

DEVTOOL_CHOICES = {
   ('django','django'),
   ('spring', 'spring'),
   ('ruby', 'ruby'),
   ('None', 'None of these'),
}

class Post(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="ideas/",null=True,blank=True)
    content=models.TextField()
    interest=models.PositiveIntegerField()
    devtool = models.CharField(max_length=80, choices=DEVTOOL_CHOICES, null=True)


    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self): #제목나오게
        return self.title 
    def summary(self): #요약
        return self.content[:50]
