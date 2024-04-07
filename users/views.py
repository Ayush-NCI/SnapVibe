"""
Module containing views for the users app.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from posts.models import Post
from .models import Profile
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm

# Create your views here.
@csrf_protect
@require_POST
def user_login(request):
    """
    View function for user login.
    """
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            user= authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect(reverse('posts:feed'))
            return HttpResponse("Invalid credentials")
    else:            
        form = LoginForm()
    return render(request,'users/login.html',{'form':form})

@login_required  
@require_POST
def index(request):
    """
    View function for index page.
    """
    current_user=request.user
    posts=Post.objects.filter(user=current_user).order_by('-created')
    profile=Profile.objects.filter(user=current_user).first()
    return render(request, 'users/index.html',{'posts':posts, 'profile':profile})

@require_POST    
def register(request):
    """
    View function for user registration.
    """
    if request.method=='POST':
        
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'users/register_done.html')
    else:
        user_form=UserRegistrationForm()
        
    return render(request,'users/register.html',{'user_form':user_form})    
    
@login_required
def edit(request):
    """
    View function for editing user info.
    """
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile,
        data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('posts:feed'))
    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)    
    return render(request,'users/edit.html',{'user_form':user_form,
    'profile_form':profile_form})    
    