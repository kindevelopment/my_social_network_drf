# Generated by Django 4.1.6 on 2023-02-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0005_alter_team_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='permit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invite',
            name='process',
            field=models.BooleanField(default=True),
        ),
    ]