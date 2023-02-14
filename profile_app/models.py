from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


def user_directory_path(instance, filename):
    return f'user_post/{instance.user.username}/{filename}'


class User(AbstractUser):
    about = models.TextField('О себе', max_length=5000)
    avatar = models.ImageField('Аватарка', upload_to='user_avatar/%Y-%m-%d/', null=True, blank=True)
    address = models.CharField('Адрес проживания', max_length=200, null=True, blank=True)
    phone_num = models.PositiveSmallIntegerField('Номер телефона', max_length=40)
    url_github = models.URLField('Ссылка на свой github', blank=True, null=True)
    follow = models.ManyToManyField(
        'self',
        related_name='followers',
        null=True,
        blank=True,
        verbose_name='Подписки'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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
        null=True,
        blank=True,
        verbose_name='Лайки'
    )
    dislikes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='user_dislikes',
        null=True,
        blank=True,
        verbose_name='Дизлайки'
    )

    def __str__(self):
        return f'{self.user.username} - {self.title}'

    class Meta:
        verbose_name = 'Пост пользователя'
        verbose_name_plural = 'Посты пользователя'


class Comments(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_comments',
        verbose_name='Автор',
    )
    text = models.TextField('Содержимое', max_length=5000)
    datetime_published = models.DateTimeField('Время публикации', auto_now_add=True)
    comment_user_post = models.ForeignKey(
        UserPost,
        on_delete=models.CASCADE,
        related_name='comments_user_post',
    )
    comment_team_post = models.ForeignKey(
        'TeamPost',
        on_delete=models.CASCADE,
        related_name='comments_team_post',
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Комментарий пользователя'
        verbose_name_plural = 'Комментарии пользователя'


