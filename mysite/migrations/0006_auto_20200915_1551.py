# Generated by Django 2.0 on 2020-09-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_measure_items_measure_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure_values',
            name='measure_time',
            field=models.DateTimeField(),
        ),
    ]
