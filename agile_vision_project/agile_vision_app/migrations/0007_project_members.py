# Generated by Django 2.1.5 on 2019-02-10 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile_vision_app', '0006_auto_20190209_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(to='agile_vision_app.Member'),
        ),
    ]