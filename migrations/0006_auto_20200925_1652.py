# Generated by Django 3.1.1 on 2020-09-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0005_setstatus_github_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_progress',
        ),
        migrations.AddField(
            model_name='book',
            name='book_setCompleted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='book_totalsets',
            field=models.IntegerField(default=0),
        ),
    ]
