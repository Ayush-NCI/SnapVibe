"""
Module containing models for the users app.
"""
from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    """
    Model representing user profile information.
    """
    user =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo =models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    objects = models.Manager()
    def __str__(self):
        """
        Return a string representation of the profile.
        """
        if hasattr(self, 'user') and hasattr(self.user, 'username'):
            return self.user.username
        return 'Profile'
        