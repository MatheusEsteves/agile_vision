# Generated by Django 2.1.5 on 2019-02-20 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile_vision_app', '0019_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(null=True),
        ),
    ]