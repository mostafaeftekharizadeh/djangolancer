# Generated by Django 3.2.12 on 2022-12-21 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_rename_offerlevel_offerstep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerstep',
            name='time',
        ),
        migrations.AddField(
            model_name='offerstep',
            name='duration',
            field=models.DurationField(default=datetime.timedelta),
        ),
    ]
