# Generated by Django 2.0 on 2020-12-07 14:53

from django.db import migrations, models
import mysite.models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_auto_20201128_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(default=1, upload_to=mysite.models.upload_path_handler_project),
            preserve_default=False,
        ),
    ]
