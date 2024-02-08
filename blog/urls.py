from . import views
from django.urls import path, include
from blog.views import PostList, PostDetail, PostLike, dashboard_view
from .views import PostDetail, dashboard_view, post_approval_view
from .views import edit_post, delete_post
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('post-approval/', views.post_approval_view, name='post_approval'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
