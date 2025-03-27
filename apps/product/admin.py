from django.contrib import admin
from .models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title",  "price", "description", "image",
                    "is_free", "created_at","file", "rate")
    list_filter = ("category", "tags","created_at")
    search_fields = ("title", "price")
    filter_horizontal = ("tags",)

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    display_genres.short_description = "Жанры"

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    display_tags.short_description = "Теги"

    def display_comments(self, obj):
        return ", ".join([comment.text for comment in obj.comments.all()])
    display_comments.short_description = "Комментарии"



class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'text', 'created_at')
    list_filter = ('created_at',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)















