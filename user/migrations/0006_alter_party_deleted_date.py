# Generated by Django 3.2.12 on 2022-10-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_language_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='deleted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]