# Generated by Django 4.1.6 on 2023-02-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0006_meeting_meeting_civicrm_c09b04_idx_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="person",
            index=models.Index(fields=["civicrm_id"], name="person_civicrm_9c9d2e_idx"),
        ),
    ]
