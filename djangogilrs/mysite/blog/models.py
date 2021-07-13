from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): ##모델을 정의하는 코드
    
    ## models: 장고모델임을 의미, Post가 데이터베이스에 저장되어야 함
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ## models.ForeignKey: 다른 모델에 대한 링크
    title = models.CharField(max_length=200)
    ## models.CharField: 글자수가 제한된 텍스트 (짧은 문자열, 주로 글제목)
    text = models.TextField()
    ## models.TextField: 글자수 제한X (블로그 컨텐츠)
    created_date = models.DateTimeField(
            default=timezone.now)
    ## models.DateTimeField: 날짜와 시간
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title