"""
Module containing urls for the users app.
"""
from django.urls import path
from . import views

# pylint: disable=C0103
app_name = 'posts'

urlpatterns = [
    path('create', views.post_create, name='create'),
    path('feed', views.feed, name='feed'),
    path('like', views.like_post, name='like'),
    path('delete/<int:user_id>/', views.post_delete, name='delete'),
]
