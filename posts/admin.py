"""
This module contains the admin views and functionalities.
"""
from django.contrib import admin
from .models import Post, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
