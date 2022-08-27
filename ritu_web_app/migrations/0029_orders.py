# Generated by Django 4.0.5 on 2022-08-27 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0028_orderdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ritu_web_app.players')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ritu_web_app.marketplace')),
            ],
        ),
    ]
