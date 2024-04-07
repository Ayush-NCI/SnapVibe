"""
Module containing views for the users app.
"""
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_safe
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreateForm, CommentForm

# Create your views here.

@login_required
@require_POST
def post_create(request):
    """
    View function for creating posts.
    """
    if request.method=='POST':
        form=PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item= form.save(commit=False)
            new_item.user=request.user
            new_item.save()
            return redirect('posts:feed')
    else:
        form =PostCreateForm(data=request.GET)
    return render(request,'posts/create.html',{'form':form})    
    
@require_GET
def feed(request):
    """
    View function for viewing all posts.
    """
    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        new_comment=comment_form.save(commit=False)
        post_id=request.POST.get('post_id')
        post=get_object_or_404(Post,id=post_id)
        new_comment.post=post
        new_comment.save()
    else:
        comment_form=CommentForm()
    posts=Post.objects.all().order_by('-created')
    logged_user=request.user
    return render(request,'posts/feed.html',{'posts':posts,
    'logged_user':logged_user, 'comment_form':comment_form})

@require_safe
def like_post(request):
    """
    View function for liking the posts.
    """
    post_id=request.POST.get('post_id')
    post=get_object_or_404(Post,id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed')    

@require_safe    
def post_delete(request, user_id):
    """
    View function for deleting the posts.
    """
    post = get_object_or_404(Post, id=user_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})    
    