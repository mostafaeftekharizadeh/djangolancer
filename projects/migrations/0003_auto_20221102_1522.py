# Generated by Django 3.2 on 2022-11-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
        ('projects', '0002_auto_20221031_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='skill',
        ),
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.ManyToManyField(to='configuration.Skill'),
        ),
    ]
