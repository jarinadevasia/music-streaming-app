# Generated by Django 4.1.3 on 2023-05-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
        migrations.AddField(
            model_name='song',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
