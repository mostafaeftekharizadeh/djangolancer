# Generated by Django 3.2.4 on 2022-08-24 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0006_alter_skill_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configuration.category'),
        ),
    ]
