from .models import Comment
from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'featured_image', 'excerpt', 'status']

    # You can add additional customizations or validations here if needed

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # You can customize the widgets or add additional attributes here if needed


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)