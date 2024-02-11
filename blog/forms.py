from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']
        widgets = {'content': SummernoteWidget()}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
