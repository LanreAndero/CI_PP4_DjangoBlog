from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment, Category, Tag


class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all()
    )
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    is_featured = forms.BooleanField(required=False)

    class Meta:
        model = Post
        fields = [
            'title', 'slug', 'author', 'featured_image',
            'excerpt', 'content', 'status'
        ]
        widgets = {'content': SummernoteWidget()}


class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    parent_comment_id = forms.IntegerField(
        required=False, widget=forms.HiddenInput
    )

    class Meta:
        model = Comment
        fields = ['body', 'name', 'email']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget = forms.Textarea(
            attrs={'rows': 4, 'placeholder': 'Your comment'}
        )
