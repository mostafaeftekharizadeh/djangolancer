# Generated by Django 4.1.4 on 2023-01-08 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_education_degree'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='source',
        ),
        migrations.AddField(
            model_name='message',
            name='party',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='source', to='user.party'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='user.party'),
        ),
    ]
