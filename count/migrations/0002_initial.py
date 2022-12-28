# Generated by Django 3.2.12 on 2022-12-14 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '0001_initial'),
        ('count', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.party'),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.status'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='count',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='count.count'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.party'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.status'),
        ),
        migrations.AddField(
            model_name='count',
            name='bankname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.bank'),
        ),
        migrations.AddField(
            model_name='count',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.party'),
        ),
        migrations.AddField(
            model_name='account',
            name='count',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='count.count'),
        ),
        migrations.AddField(
            model_name='account',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.party'),
        ),
    ]