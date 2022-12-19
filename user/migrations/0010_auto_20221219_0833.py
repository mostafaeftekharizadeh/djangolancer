# Generated by Django 3.2.12 on 2022-12-19 08:33

from django.db import migrations, models
import user.profile_models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_merge_20221219_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='work_place',
        ),
        migrations.RemoveField(
            model_name='worksample',
            name='work_file',
        ),
        migrations.AddField(
            model_name='worksample',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=user.profile_models.WorkSample.hash_upload),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
