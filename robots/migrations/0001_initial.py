# Generated by Django 4.2.5 on 2023-09-27 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=5)),
                ('model', models.CharField(max_length=2)),
                ('version', models.CharField(max_length=2)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_ordered', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Робот',
                'verbose_name_plural': 'Роботы',
                'ordering': ['serial'],
            },
        ),
    ]
