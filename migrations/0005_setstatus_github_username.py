# Generated by Django 3.1.1 on 2020-09-14 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0004_auto_20200914_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='setstatus',
            name='github_username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='IIT_OpenOCR.users'),
        ),
    ]
