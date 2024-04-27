from django.urls import path
from allauth.account.views import SignupView
from .views import (
    about_view,
    dashboard_view,
    edit_post,
    delete_post,
    post_approval_view,
    PostList,
    PostDetail,
    PostLike,
)

urlpatterns = [
    # Public URLs
    path('about/', about_view, name='about'),
    path('', PostList.as_view(), name='home'),
    path('detail/<slug:slug>/', PostDetail.as_view(), name='post_detail'),

    # User Authentication URLs
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),

    # User Dashboard URLs
    path('dashboard/', dashboard_view, name='dashboard'),

    # Post Management URLs
    path('post-approval/', post_approval_view, name='post_approval'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),

    # Like/Dislike Post URLs
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
]
