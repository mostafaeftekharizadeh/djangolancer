# Generated by Django 4.2.5 on 2023-11-13 12:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0008_message_is_seen_alter_message_media"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="is_seen",
        ),
    ]