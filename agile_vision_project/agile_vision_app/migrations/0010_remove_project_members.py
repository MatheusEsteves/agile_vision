# Generated by Django 2.1.5 on 2019-02-10 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agile_vision_app', '0009_auto_20190210_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
    ]
