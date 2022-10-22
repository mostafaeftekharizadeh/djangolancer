# Generated by Django 3.2.12 on 2022-10-22 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('exp_opinion', models.TextField(null=True)),
                ('complain_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.complaintype')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complain_owner', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complain_user', to=settings.AUTH_USER_MODEL)),
                ('viewstatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.viewstatus')),
            ],
        ),
        migrations.CreateModel(
            name='ResultComplain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('resulte', models.TextField()),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('complain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complain.complain')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.status')),
            ],
        ),
    ]
