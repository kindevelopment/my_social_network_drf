from django.conf import settings
from django.db import models


class Message(models.Model):
    user_sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Отправитель',
        related_name='user_sender_messages',
    )
    user_reciever = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Получатель',
        related_name='user_reciever_messages',
    )
    text_message = models.TextField('Содержимое')
    hide = models.JSONField(default=list, blank=True)
    time_send_message = models.DateTimeField('Время отправки', auto_now_add=True)

    def __str__(self):
        return f'{self.user_sender.username} - {self.user_reciever.username}'

    class Meta:
        verbose_name = 'Сообщение пользователя'
        verbose_name_plural = 'Сообщении пользователей'

