# Generated by Django 4.1.3 on 2023-05-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_song_last_played'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('audio_file', models.FileField(upload_to='songs/favourite/')),
                ('duration', models.FloatField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='artist',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
