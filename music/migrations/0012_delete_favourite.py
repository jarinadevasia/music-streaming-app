# Generated by Django 4.1.3 on 2023-05-06 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_alter_song_artist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favourite',
        ),
    ]
