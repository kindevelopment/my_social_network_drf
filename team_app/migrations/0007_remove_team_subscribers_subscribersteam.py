# Generated by Django 4.1.6 on 2023-02-21 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team_app', '0006_invite_permit_invite_process'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='subscribers',
        ),
        migrations.CreateModel(
            name='SubscribersTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_moder', models.BooleanField(default=False, verbose_name='Модератор команды')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_users_team', to='team_app.team', verbose_name='Команда')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]