from django.conf import settings
from django.db import models


def team_directory_path(instance, filename):
    return f'team_avatar/team-{instance.title}/{filename}'


class Team(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Создатель команды',
    )
    title = models.CharField('Название команды', max_length=150)
    about = models.TextField('О команде')
    avatar = models.ImageField('Аватарка команды', upload_to=team_directory_path, null=True, blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='Категория',
    )
    stack = models.ManyToManyField(
        'Stack',
        related_name='all_team_in_stack',
        verbose_name='Стек',
    )
    subscribers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='all_subscribers_post',
        verbose_name='Подписчики команды',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class TeamPost(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор поста',
    )
    title = models.CharField('Название поста')
    text = models.TextField('Содержимое')
    poster = models.ImageField('Постер поста', upload_to='team_post_poster/', null=True, blank=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='likes_post_team',
        null=True,
        blank=True,
        verbose_name='Лайки',
    )
    dislikes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='dislikes_post_team',
        null=True,
        blank=True,
        verbose_name='Дизлайки',
    )
    team_post = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='all_post_in_team',
        verbose_name='Пост команды',
    )

    def __str__(self):
        return f'{self.team_post.title} - {self.title}'

    class Meta:
        verbose_name = 'Пост команды'
        verbose_name_plural = 'Посты команды'


class Category(models.Model):
    title = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Stack(models.Model):
    title = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стек'
        verbose_name_plural = 'Стек'


class Invite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        verbose_name='Команда',
    )
    datetime_push_invite = models.DateTimeField('Время отправки', auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.team.title}'

    class Meta:
        verbose_name = 'Заявка на вступление'
        verbose_name_plural = 'Заявки на вступление'

