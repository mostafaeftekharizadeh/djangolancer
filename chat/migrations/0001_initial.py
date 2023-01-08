# Generated by Django 4.1.4 on 2023-01-08 08:52

import chat.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0017_alter_offer_state'),
        ('user', '0012_alter_education_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('media', models.ImageField(blank=True, null=True, upload_to=chat.models.Message.hash_upload)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='user.party')),
                ('target', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='user.party')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
