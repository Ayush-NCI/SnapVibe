from .models import Post, Comment
from django import forms

class PostCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].error_messages = {'required': '*'}
        self.fields['image'].error_messages = {'required': '*'}
        self.fields['caption'].error_messages = {'required': '*'}
    class Meta:
        model=Post
        fields=('title','image','caption')
       
        
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].error_messages = {'required': '*'}
        self.fields['posted_by'].error_messages = {'required': '*'}
    class Meta:
        model=Comment
        fields=('body','posted_by',)
        
       