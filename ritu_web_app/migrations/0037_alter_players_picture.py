# Generated by Django 4.0.5 on 2022-08-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0036_alter_leaderboard_earnedpoints_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='picture',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images/'),
        ),
    ]
