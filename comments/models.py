from django.conf import settings
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    text = models.TextField('Содержимое', max_length=5000)
    datetime_published = models.DateTimeField('Время публикации', auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Комментарий пользователя'
        verbose_name_plural = 'Комментарии пользователей'
        abstract = True
