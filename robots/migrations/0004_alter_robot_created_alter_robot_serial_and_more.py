# Generated by Django 4.2.5 on 2023-09-26 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0003_alter_robot_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 10, 26, 10, 834184, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='robot',
            name='serial',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='robot',
            name='version',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]