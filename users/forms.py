"""
Module containing form definitions for the users app.
"""
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    """
    Form for login the user.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm): 
    """
    Form for creating user information.
    """
    password=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        """
        Metadata for the UserRegistrationForm.

        Specifies the associated User model and fields for the form.
        """
        model=User
        fields={'username','email','first_name', 'last_name'}
        
    def check_password(self):
        """
        Method to check if the entered passwords match.

        Returns:
            str: The confirmed password.

        Raises:
            forms.ValidationError: If the passwords do not match.
        """
        if self.cleaned_data['password']!=self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data['password2']   
        
class UserEditForm(forms.ModelForm):
    """
    Form for editing user information.
    """
    class Meta:
        """
        Metadata for the UserEditForm.

        Specifies the associated User model and fields for the form.
        """
        model=User
        fields=('first_name','last_name','email')
        
class ProfileEditForm(forms.ModelForm):
    """
    Form for creating/editing user profile information.
    """
    class Meta:
        """
        Metadata for the ProfileEditForm.

        Specifies the associated Profile model and fields for the form.
        """
        model=Profile
        fields=('photo',) 
        