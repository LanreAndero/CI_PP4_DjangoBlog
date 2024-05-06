from django import forms
from .models import Post, Comment, Category, Tag


class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    is_featured = forms.BooleanField(required=False)

    content = forms.Textarea()

    class Meta:
        model = Post
        fields = [
            'title', 'author', 'content', 'categories', 'tags',
            'is_featured', 'featured_image'
        ]

        labels = {
            'title': 'Title',
            'author': 'Author',
            'content': 'Content',
            'categories': 'Category',
            'tags': 'Tags',
            'is_featured': 'Is Featured',
            'featured_image': 'Featured Image'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.HiddenInput(),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 10}
            ),
            'featured_image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['categories'].required = True
        self.fields['tags'].required = True


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
