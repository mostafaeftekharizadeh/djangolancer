# Generated by Django 3.2.12 on 2022-12-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20221221_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='price',
            new_name='cost',
        ),
        migrations.AlterField(
            model_name='offerstep',
            name='optional',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
