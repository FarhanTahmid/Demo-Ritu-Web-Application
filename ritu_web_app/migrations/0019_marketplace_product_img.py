# Generated by Django 4.0.5 on 2022-08-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0018_leaderboard_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplace',
            name='product_img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image'),
        ),
    ]
