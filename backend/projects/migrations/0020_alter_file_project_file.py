# Generated by Django 4.1.4 on 2023-02-02 14:57

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_project_exp_time_project_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='project_file',
            field=models.FileField(blank=True, null=True, upload_to=projects.models.File.hash_upload),
        ),
    ]
