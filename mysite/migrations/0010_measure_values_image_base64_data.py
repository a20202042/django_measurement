# Generated by Django 2.0 on 2020-09-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20200918_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='measure_values',
            name='image_base64_data',
            field=models.TextField(default=1, max_length=10000),
            preserve_default=False,
        ),
    ]
