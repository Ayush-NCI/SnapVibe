"""
Module containing application configuration for the 'users' app.
"""
from django.apps import AppConfig

class UsersConfig(AppConfig):
    """
    Application configuration class for the 'users' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
