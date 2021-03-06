# Generated by Django 2.1.5 on 2019-02-11 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile_vision_app', '0012_auto_20190210_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectteam',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectteam',
            name='team',
        ),
        migrations.AddField(
            model_name='team',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='teams', to='agile_vision_app.Project'),
        ),
        migrations.DeleteModel(
            name='ProjectTeam',
        ),
    ]
