# Generated by Django 4.0.4 on 2022-05-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_movie_budget_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
