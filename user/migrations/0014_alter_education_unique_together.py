# Generated by Django 3.2.12 on 2022-11-16 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0004_alter_estimate_name'),
        ('user', '0013_alter_specialty_party'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='education',
            unique_together={('party', 'degree')},
        ),
    ]
