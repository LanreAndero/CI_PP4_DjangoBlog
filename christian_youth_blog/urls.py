from django.contrib import admin
from django.urls import path, include
from blog.views import add_post_view, search, PostDetail, PostList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('home', include('blog.urls')),
    path('blog/', PostList.as_view(), name='blog'),
    path('search/', search, name='search'),
    path('add-post/', add_post_view, name='add_post'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
