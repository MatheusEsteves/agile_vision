# Generated by Django 2.1.5 on 2019-02-20 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile_vision_app', '0020_auto_20190220_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
