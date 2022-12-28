# Generated by Django 3.2.12 on 2022-12-19 06:40

from django.db import migrations, models
import user.profile_models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20221217_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksample',
            name='work_file',
            field=models.FileField(blank=True, null=True, upload_to=user.profile_models.WorkSample.hash_upload),
        ),
    ]