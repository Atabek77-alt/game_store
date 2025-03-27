from django.contrib import admin
from .models import GameNews


@admin.register(GameNews)
class GameNewsAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'description',
        'image',

]
    search_fields = ['title']
    ordering = ['-created_at']
    filter_horizontal = ('tags','category')

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Теги'


    def get_news_detail(self, obj):
        return obj.game_detail.title
    get_news_detail.short_description = 'Игры'


    def get_category(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_tags.short_description = 'Категории'

