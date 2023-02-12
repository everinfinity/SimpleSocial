# Generated by Django 4.1.6 on 2023-02-12 02:12

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("magazine", "0020_archivearticle_magazine_ar_drupal__fd3a5b_idx"),
    ]

    operations = [
        migrations.AlterField(
            model_name="archivearticleauthor",
            name="article",
            field=modelcluster.fields.ParentalKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="archive_authors",
                to="magazine.archivearticle",
            ),
        ),
    ]
