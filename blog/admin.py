from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('name', 'email', 'body', 'created_on', 'approved')
    can_delete = False
    show_change_link = True


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    inlines = [CommentInline]

    list_display = ('title', 'slug', 'status', 'created_on', 'approved')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'approved')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['approve_posts', 'unpublish_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)

    def unpublish_posts(self, request, queryset):
        queryset.update(approved=False)

    approve_posts.short_description = "Approve selected posts"
    unpublish_posts.short_description = "Unpublish selected posts"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments', 'delete_selected']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    approve_comments.short_description = "Approve selected comments"
