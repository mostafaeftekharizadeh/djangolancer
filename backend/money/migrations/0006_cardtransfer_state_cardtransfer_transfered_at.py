# Generated by Django 4.1.4 on 2022-12-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0005_alter_cardtransfer_shaba'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtransfer',
            name='state',
            field=models.CharField(blank=True, choices=[('i', 'In Progress'), ('p', 'Completed')], default='i', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='cardtransfer',
            name='transfered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
