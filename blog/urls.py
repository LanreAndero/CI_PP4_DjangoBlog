from . import views
from django.urls import path
from blog.views import PostList, PostDetail, dashboard_view
from allauth.account.views import SignupView
from .views import edit_post, delete_post, about_view


urlpatterns = [
    path('about/', about_view, name='about'),
    path('', PostList.as_view(), name='home'),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('post-approval/', views.post_approval_view, name='post_approval'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
