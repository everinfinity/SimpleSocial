# Generated by Django 4.2.1 on 2023-05-04 14:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("subscription", "0002_auto_20220706_1744"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subscription",
            old_name="format",
            new_name="magazine_format",
        ),
    ]
