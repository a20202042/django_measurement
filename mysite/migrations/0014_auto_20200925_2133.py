# Generated by Django 2.0 on 2020-09-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20200924_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure_image',
            name='image',
            field=models.ImageField(upload_to='measure_item/'),
        ),
        migrations.AlterField(
            model_name='measure_items',
            name='image',
            field=models.ImageField(upload_to='measure_item/111.png'),
        ),
    ]
