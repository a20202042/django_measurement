# Generated by Django 2.0 on 2020-08-26 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement_work_order_create',
            name='project_measure',
            field=models.ForeignKey(db_column='project', on_delete=django.db.models.deletion.CASCADE, to='mysite.project'),
        ),
    ]
