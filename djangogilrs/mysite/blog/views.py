from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
# 요청(request)을 넘겨받아 render메서드를 호출
# render 메서드를 호출하여 받은(return) blog/post_list.html템플릿을 보여줌
