"""
Module containing form definitions for the posts app.
"""
from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    """
    Form for creating the post.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].error_messages = {'required': '*'}
        self.fields['image'].error_messages = {'required': '*'}
        self.fields['caption'].error_messages = {'required': '*'}
    class Meta:
        """
        Metadata for the PostCreateForm.

        Specifies the associated Post model and fields for the form.
        """
        model=Post
        fields=('title','image','caption')
       
        
class CommentForm(forms.ModelForm):
    """
    Form for comment.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].error_messages = {'required': '*'}
        self.fields['posted_by'].error_messages = {'required': '*'}
        
    class Meta:
        """
        Metadata for the CommentForm.

        Specifies the associated comment model and fields for the form.
        """
        model=Comment
        fields=('body','posted_by',)
        