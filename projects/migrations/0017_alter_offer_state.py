# Generated by Django 4.1.4 on 2022-12-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_offerstep_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='state',
            field=models.CharField(blank=True, choices=[('a', 'Accept'), ('r', 'Reject'), ('n', 'Not Set'), ('p', 'Paid')], default='n', max_length=1, null=True),
        ),
    ]
