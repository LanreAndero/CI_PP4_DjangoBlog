from . import views
from django.urls import path, include
from .views import custom_login
from blog.views import PostList, PostDetail, PostLike
from .views import PostDetail, dashboard_view


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('login/', custom_login, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
