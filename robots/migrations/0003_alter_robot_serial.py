# Generated by Django 4.2.5 on 2023-09-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0002_alter_robot_options_remove_robot_is_ordered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='serial',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
