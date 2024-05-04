from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from allauth.account.forms import SignupForm
from .models import Post
from django.contrib import messages
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.text import slugify


def should_approve_user_posts():
    print("Checking whether user posts should be approved")
    return settings.SHOULD_APPROVE_USER_POSTS


def signup_view(request):
    form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


def about_view(request):
    return render(request, 'about.html')


def index_view(request):
    return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = (
        Post.objects
        .filter(status=1, approved=True)
        .order_by("-created_on")
    )
    template_name = "blog.html"
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
def add_post_view(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            if not post.slug or post.slug == 'placeholder':
                post.slug = slugify(post.title)
                if Post.objects.filter(slug=post.slug).exists():
                    post.slug = f"{post.slug}-{post.id}"
            if should_approve_user_posts():
                post.approved = False
                messages.success(
                    request, 'Post created and awaiting approval!'
                )
            else:
                post.approved = True
                messages.success(request, 'Post created successfully!')
            post.save()
            return redirect('blog')
        else:
            messages.error(
                request, 'Error creating post. Please check the form.'
            )
    else:
        post_form = PostForm()

    user_posts = Post.objects.filter(author=request.user)
    return render(
        request, 'add_post.html',
        {'post_form': post_form, 'user_posts': user_posts}
    )


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(
        request, 'edit_post.html',
        {'form': form, 'post': post}
    )


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_detail')
    return render(request, 'delete_post.html', {'post': post})


@staff_member_required
def post_approval_view(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        action = request.POST.get('action')
        post = get_object_or_404(Post, id=post_id)
        if action == 'approve':
            post.approved = True
            post.save()
            messages.success(request, 'Post approved successfully!')
        elif action == 'reject':
            post.delete()
            messages.success(request, 'Post rejected successfully!')
    pending_posts = Post.objects.filter(approved=False)
    return render(
        request,
        'post_approval.html',
        {'pending_posts': pending_posts}
    )


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(
            reverse('post_detail', args=[slug])
        )


def search(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(title__icontains=query)
    else:
        results = None
    return render(
        request, 'search_results.html', {'results': results, 'query': query}
    )
