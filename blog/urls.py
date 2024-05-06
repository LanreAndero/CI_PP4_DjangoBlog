from django.urls import path
from allauth.account.views import SignupView
from . import views
from .views import edit_post, delete_post


urlpatterns = [
    path('', views.index_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('search/', views.search, name='search'),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    # path('post-list/', views.PostList.as_view(), name='post_list'),
    path(
        'post-detail/<slug:slug>/',
        views.PostDetail.as_view(), name='post_detail'
    ),
    path('add-post/', views.add_post_view, name='add_post'),
    path('post-approval/', views.post_approval_view, name='post_approval'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('post-like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
