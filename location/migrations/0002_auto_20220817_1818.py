# Generated by Django 3.2.4 on 2022-08-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='country',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='place',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='state',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
