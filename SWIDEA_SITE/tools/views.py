from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm

def tool_list(request):
    tools = Post.objects.all()
    ctx={'tools':tools}

    return render(request,template_name='tool_list.html',context=ctx)

    
def tool_detail(request,pk):    
    tools=get_object_or_404(Post, pk=pk)
    ctx={'tools':tools}
    
    return render(request,'tool_detail.html.',context=ctx)

def tool_create(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save()
            return redirect('tools:tool_detail',post.pk)
            
    else:
        form=PostForm
        ctx={'form':form}

        return render(request, template_name='tool_create.html',context=ctx)


def tool_update(request,pk):
    post = get_object_or_404(Post,id=pk)
    
    if request.method=='POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save()
            return redirect('tools:tool_detail',pk)
    else:
        form=PostForm(instance=post)
        ctx={'form':form} 
        return render(request,template_name='tool_create_update.html',context=ctx)


def tool_delete(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('tools:tool_list')