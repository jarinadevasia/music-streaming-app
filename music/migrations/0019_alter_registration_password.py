# Generated by Django 4.1.3 on 2023-05-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0018_alter_registration_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
