# Generated by Django 4.0.4 on 2022-05-21 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Move',
            new_name='Movie',
        ),
    ]
