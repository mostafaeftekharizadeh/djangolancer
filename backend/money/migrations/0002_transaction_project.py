# Generated by Django 4.1.4 on 2022-12-29 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_alter_offer_state'),
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]