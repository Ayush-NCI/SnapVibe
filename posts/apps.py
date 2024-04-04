"""
Module containing application configuration for the 'posts' app.
"""
from django.apps import AppConfig

class PostsConfig(AppConfig):
    """
    Application configuration class for the 'posts' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    
