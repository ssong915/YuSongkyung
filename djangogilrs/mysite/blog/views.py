from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})
# 요청(request)을 넘겨받아 render메서드를 호출
# render 메서드를 호출하여 받은(return) blog/post_list.html템플릿을 보여줌