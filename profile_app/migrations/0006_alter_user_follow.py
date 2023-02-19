# Generated by Django 4.1.6 on 2023-02-16 09:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0005_alter_user_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]