# Generated by Django 4.1.6 on 2023-02-08 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0016_event_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="sponsor",
        ),
    ]
