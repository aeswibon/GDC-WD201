# Generated by Django 4.0.2 on 2022-02-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='report_time',
        ),
        migrations.AddField(
            model_name='report',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]