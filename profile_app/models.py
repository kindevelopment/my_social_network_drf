from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from team_app.models import TeamPost

from comments.models import Comment


def user_directory_path(instance, filename):
    return f'user/user_post/{instance.user.username}/{filename}'


class User(AbstractUser):
    about = models.TextField('О себе', max_length=5000)
    avatar = models.ImageField('Аватарка', upload_to='user/user_avatar/%Y-%m-%d/', null=True, blank=True)
    address = models.CharField('Адрес проживания', max_length=200, null=True, blank=True)
    phone_num = models.PositiveSmallIntegerField('Номер телефона', null=True, blank=True)
    url_github = models.URLField('Ссылка на свой github', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Subscribe(models.Model):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followers', verbose_name='Подписчики')   # кто подписан на меня
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='user_follow_following', on_delete=models.CASCADE)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='follow', verbose_name='Подписки')         # На кого я подписан

    class Meta:
        verbose_name = 'Подписки и подписчики'
        verbose_name_plural = 'Подписки и подписчики'


class UserPost(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_posts',
        verbose_name='Автор'
    )
    title = models.CharField('Название', max_length=250)
    text = models.TextField('Содержимое')
    poster = models.ImageField('Постер', upload_to=user_directory_path, null=True, blank=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='user_likes',
        blank=True,
        verbose_name='Лайки'
    )
    dislikes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='user_dislikes',
        blank=True,
        verbose_name='Дизлайки'
    )

    def __str__(self):
        return f'{self.user.username} - {self.title}'

    class Meta:
        verbose_name = 'Пост пользователя'
        verbose_name_plural = 'Посты пользователей'


class CommentUserPost(Comment):
    comment_user_post = models.ForeignKey(
        UserPost,
        on_delete=models.CASCADE,
        related_name='comments_user_post',
        verbose_name='Комментарии к посту пользователя',
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Комментарий пользователя'
        verbose_name_plural = 'Комментарии пользователей'
