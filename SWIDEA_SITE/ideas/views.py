from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
import tools.models


def idea_list(request):
    ideas = Post.objects.all()
    ctx={'ideas':ideas}

    return render(request,template_name='idea_list.html',context=ctx)

    
def idea_detail(request,pk):    
    ideas=get_object_or_404(Post, pk=pk)
    ctx={'ideas':ideas}
    
    return render(request,'idea_detail.html.',context=ctx)

def idea_create(request):
    if request.method =='POST': #post-저장하기 눌렀을때, 생성하고, 수정할때
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save()
            return redirect('ideas:idea_list')
            
    else: #get 
        form=PostForm
        ctx={'form':form}

        return render(request, template_name='idea_create.html',context=ctx)


def idea_update(request,pk):
    #index pk를 가지고 있는 넘을 가지고 와야댐
    post = get_object_or_404(Post,id=pk) #DB에 이미 있는 넘 가져오기 id 해당하는 것만 
    
    if request.method=='POST':
        form = PostForm(request.POST,instance=post)#instance=post: 가지고 온 객체를 넣어주기
        if form.is_valid():
            post=form.save()
            return redirect('ideas:idea_detail',pk)#pk가지고 상세페이지로 이동
    else: #get 
        form=PostForm(instance=post)
        ctx={'form':form} #form이라는 이름의 form
        return render(request,template_name='idea_create_update.html',context=ctx)


def idea_delete(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('ideas:idea_list')