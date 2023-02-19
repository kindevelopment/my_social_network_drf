# Generated by Django 4.1.6 on 2023-02-15 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import team_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Стек',
                'verbose_name_plural': 'Стек',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название команды')),
                ('about', models.TextField(verbose_name='О команде')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=team_app.models.team_directory_path, verbose_name='Аватарка команды')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='team_app.category', verbose_name='Категория')),
                ('stack', models.ManyToManyField(related_name='all_team_in_stack', to='team_app.stack', verbose_name='Стек')),
                ('subscribers', models.ManyToManyField(related_name='all_subscribers_post', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики команды')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель команды')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.CreateModel(
            name='TeamPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название поста')),
                ('text', models.TextField(verbose_name='Содержимое')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='team_post_poster/', verbose_name='Постер поста')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes_post_team', to=settings.AUTH_USER_MODEL, verbose_name='Дизлайки')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes_post_team', to=settings.AUTH_USER_MODEL, verbose_name='Лайки')),
                ('team_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_post_in_team', to='team_app.team', verbose_name='Пост команды')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
            ],
            options={
                'verbose_name': 'Пост команды',
                'verbose_name_plural': 'Посты команды',
            },
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_push_invite', models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team_app.team', verbose_name='Команда')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заявка на вступление',
                'verbose_name_plural': 'Заявки на вступление',
            },
        ),
    ]
