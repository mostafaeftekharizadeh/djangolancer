# Generated by Django 3.2.8 on 2022-12-19 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20221219_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='skill',
        ),
    ]
