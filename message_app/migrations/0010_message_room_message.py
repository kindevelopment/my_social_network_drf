# Generated by Django 4.1.6 on 2023-02-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0009_alter_message_hide'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='room_message',
            field=models.JSONField(default=list),
        ),
    ]
