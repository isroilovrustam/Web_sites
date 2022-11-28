from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


@admin.register(Comment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
    list_filter = ['post']

# @admin.register(Post)
# class PostsAdmin(admin.ModelAdmin):
#     list_display = ['title', 'summary', 'data']
#     list_filter = ['title']


admin.site.register(Post, PostAdmin)
