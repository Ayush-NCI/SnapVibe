from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

app_name = 'posts'
urlpatterns = [
    path('create', views.post_create, name='create'),
    path('feed', views.feed, name='feed'),
    path('like', views.like_post, name='like'),
    path('delete/<int:id>/', views.post_delete, name='delete'),
]