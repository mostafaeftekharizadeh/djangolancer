# Generated by Django 3.2.12 on 2022-12-14 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_alter_category_parent'),
        ('projects', '0003_auto_20221214_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cre_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuration.currency'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuration.status'),
        ),
    ]
