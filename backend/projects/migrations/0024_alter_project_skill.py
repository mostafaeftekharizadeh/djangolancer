# Generated by Django 4.2.5 on 2023-11-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("configuration", "0004_status_default"),
        ("projects", "0023_file_create_date_file_is_last_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="skill",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="project_skill",
                to="configuration.skill",
            ),
        ),
    ]
