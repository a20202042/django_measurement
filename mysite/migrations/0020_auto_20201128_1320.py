# Generated by Django 2.0 on 2020-11-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0019_auto_20201128_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure_values',
            name='time_now',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
