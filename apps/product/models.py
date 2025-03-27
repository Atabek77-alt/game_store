from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория поста'
        verbose_name_plural = 'Категории постов'

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='category_game')
    image = models.ImageField(upload_to='images3/')
    file = models.FileField(upload_to='over_all/files/',null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tag_game')
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    is_free = models.BooleanField(default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    rate = models.FloatField(default=0)
    genre  = models.ManyToManyField('Genre', related_name='genre_games')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_comments', blank=True,null=True, )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.user.username if self.user else 'Аноним'} на {self.game.title}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'








