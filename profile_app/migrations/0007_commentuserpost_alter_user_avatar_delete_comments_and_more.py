# Generated by Django 4.1.6 on 2023-02-17 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0006_alter_user_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentUserPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Содержимое')),
                ('datetime_published', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('comment_user_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user_post', to='profile_app.userpost', verbose_name='Комментарии к посту пользователя')),
            ],
            options={
                'verbose_name': 'Комментарий пользователя',
                'verbose_name_plural': 'Комментарии пользователей',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user/user_avatar/%Y-%m-%d/', verbose_name='Аватарка'),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='commentuserpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]