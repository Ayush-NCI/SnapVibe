"""
Module containing urls for the users app.
"""
from django.urls import path
from . import views

APP_NAME = 'POSTS'

urlpatterns = [
    path('create', views.post_create, name='create'),
    path('feed', views.feed, name='feed'),
    path('like', views.like_post, name='like'),
    path('delete/<int:id>/', views.post_delete, name='delete'),
]
