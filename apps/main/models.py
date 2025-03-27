from django.db import models


class ContactUs(models.Model):
    email = models.EmailField('Электронная почта', max_length=70)
    text = models.TextField('Текст')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'