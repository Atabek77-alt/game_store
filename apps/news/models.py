from django.db import models
from ..product.models import Game, Tag, Category, Comment


class GameNews(models.Model):
    title = models.CharField('Название новости', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Фото news', upload_to='new_images/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='news_tag' )
    category = models.ManyToManyField(Category, related_name='news_category')
    comment =  models.ManyToManyField(Comment, related_name='news_comment', blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


