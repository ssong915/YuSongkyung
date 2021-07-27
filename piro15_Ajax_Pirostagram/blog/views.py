from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from .forms import PostForm

import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def post_list(request):
    posts = Post.objects.all() #posts들 가져오기
    comments = Comment.objects.all() #post에 해당하는 comment 가져오기
    ctx={'posts':posts,'comments':comments}

    return render(request,template_name='post_list.html',context=ctx)

def post_create(request):    
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('blog:post_list')

    form=PostForm
    ctx={'form':form}
    return render(request, template_name='post_create.html',context=ctx)



@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body) #json -> python 으로 바꿔주는 것
                                 
    post_id = req['id']

    post = Post.objects.get(id=post_id)
    if(post.like==1):
        post.like=0
    else:
        post.like=1

    post.save()

    return JsonResponse({'id': post_id})

@csrf_exempt
def create_ajax(request):
    req = json.loads(request.body)

    post_id = req['id']
    comment = req['comment']

    post=Post.objects.get(id=post_id)
    created_comment = Comment.objects.create(post=post, comment=comment)

    created_comment.save()
    post.save()

    return JsonResponse({'id': post_id, 'comment_id': created_comment.id, 'comment': created_comment.comment })

    

@csrf_exempt
def delete_ajax(request):
    req = json.loads(request.body)
    comment_id = req['id']

    
    comment=Comment.objects.get(id=comment_id)
    comment.delete()

    return JsonResponse({'id': comment_id})

