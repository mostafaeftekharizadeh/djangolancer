# Generated by Django 3.2.4 on 2022-08-24 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='exp_opinion',
            field=models.TextField(null=True),
        ),
    ]
