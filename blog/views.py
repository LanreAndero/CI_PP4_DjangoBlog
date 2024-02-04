from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.utils.safestring import mark_safe
from django.urls import reverse
from .forms import PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['post_form'] = PostForm()  # Add this line
        return context

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

@login_required
def dashboard_view(request):
    # Fetch posts for the logged-in user
    user_posts = Post.objects.filter(author=request.user).order_by("-created_on")

    # If the form is submitted, process it
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.slug = slugify(post.title)  # Set the slug based on the title
            post.author = request.user  # Assuming you're associating the post with the current user
            post.save()
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        post_form = PostForm()

    return render(
        request,
        "dashboard.html",
        {"user_posts": user_posts, "post_form": PostForm()}
    )

def custom_login(request, *args, **kwargs):
    # Call Django's built-in login view
    response = auth_views.login(request, *args, **kwargs)

    # Check if the login was successful
    if request.user.is_authenticated:
        # Check if the user has created a post
        if request.user.blog_posts.exists():
            # User has created a post, display a welcome message
            messages.info(request, 'Welcome back! Check out the latest blog posts.')
        else:
            # User hasn't created a post, display a message with a link to create one
            messages.info(request, 'Welcome! You haven\'t created a post yet. <a href="{% url \'dashboard\' %}">Create Post</a>')

    return response


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
