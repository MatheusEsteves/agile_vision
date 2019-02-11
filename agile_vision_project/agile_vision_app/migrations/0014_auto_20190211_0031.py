# Generated by Django 2.1.5 on 2019-02-11 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agile_vision_app', '0013_auto_20190211_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolidaysPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Holidays Period',
                'verbose_name_plural': 'Holidays Periods',
            },
        ),
        migrations.RemoveField(
            model_name='memberholidays',
            name='member',
        ),
        migrations.DeleteModel(
            name='MemberHolidays',
        ),
        migrations.AddField(
            model_name='member',
            name='last_holiday_period',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='agile_vision_app.HolidaysPeriod'),
        ),
    ]
