from django.db import models
from ..accounts.models import User





class Post(models.Model):
    title = models.CharField('Название поста', max_length=100)
    text = models.TextField('Text')
    image = models.ImageField('Фото поста', upload_to='posts')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostCommentary(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment_text = models.TextField('Комментарий')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.user.username if self.user else 'Аноним'} на {self.post.title}"

    class Meta:
        verbose_name = 'Комментарий к посту'
        verbose_name_plural = 'Комментарии к постам'

