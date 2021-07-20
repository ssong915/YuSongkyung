from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import IdeaForm

#IDEAS

def idea_list(request):
    ideas = Post.objects.all()
    ctx={'ideas':ideas}

    return render(request,template_name='idea_list.html',context=ctx)


def idea_detail(request,pk):    
    ideas=get_object_or_404(Post, pk=pk)
    ctx={'ideas':ideas}

    return render(request,'idea_detail.html.',context=ctx)

def idea_create(request):
    
    form=IdeaForm(request.POST,request.FILES)
    if form.is_valid():
        new_idea=form.save(commit=False)
        new_idea.save()
        return redirect('ideas:idea_detail',new_idea.pk)

    form=IdeaForm
    ctx={'form':form}
    return render(request, template_name='idea_create.html',context=ctx)


def idea_update(request,pk):
    post = get_object_or_404(Post,id=pk)

    form=IdeaForm(request.POST,request.FILES,instance=post)
    if form.is_valid():
        new_idea=form.save(commit=False)
        new_idea.save()
        return redirect('ideas:idea_detail',pk)

    form=IdeaForm(instance=post)
    ctx={'form':form}
    return render(request, template_name='idea_create_update.html',context=ctx)

def idea_delete(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('ideas:idea_list') 