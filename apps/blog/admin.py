from django.contrib import admin
from .models import Post,  PostCommentary


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'text',
        'image',
        'created_at',
        'display_author',

    ]
    list_filter = ['created_at']
    search_fields = ['title']

    def display_author(self, obj):
        return obj.user.username if obj.user else 'Unknown'

    display_author.short_description = 'Author'




@admin.register(PostCommentary)
class PostCommentaryAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'comment_text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'post__title']
from django.contrib import admin

# Register your models here.
