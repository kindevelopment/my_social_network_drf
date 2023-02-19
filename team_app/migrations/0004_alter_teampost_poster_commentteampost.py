# Generated by Django 4.1.6 on 2023-02-17 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team_app', '0003_alter_team_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampost',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='team/team_post_poster/', verbose_name='Постер поста'),
        ),
        migrations.CreateModel(
            name='CommentTeamPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Содержимое')),
                ('datetime_published', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('comment_team_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_team_post', to='team_app.teampost', verbose_name='Комментарии к посту в команде')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий пользователя',
                'verbose_name_plural': 'Комментарии пользователей',
                'abstract': False,
            },
        ),
    ]