# Generated by Django 2.0 on 2020-11-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0018_measure_values_time_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure_values',
            name='time_now',
            field=models.DateField(auto_now=True),
        ),
    ]
