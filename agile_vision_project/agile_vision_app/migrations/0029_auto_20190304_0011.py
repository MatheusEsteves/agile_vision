# Generated by Django 2.1.7 on 2019-03-04 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agile_vision_app', '0028_auto_20190225_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='next_holidays_end_date',
            new_name='next_vacation_end_date',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='next_holidays_start_date',
            new_name='next_vacation_start_date',
        ),
    ]
