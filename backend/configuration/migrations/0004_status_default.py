# Generated by Django 4.1.4 on 2023-02-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0003_auto_20221215_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]