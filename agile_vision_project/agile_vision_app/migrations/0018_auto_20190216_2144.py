# Generated by Django 2.1.5 on 2019-02-16 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agile_vision_app', '0017_auto_20190216_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='agile_vision_app.Project'),
        ),
    ]