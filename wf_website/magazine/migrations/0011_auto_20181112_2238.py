# Generated by Django 2.1.3 on 2018-11-12 22:38

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0010_auto_20181112_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazineissuefeaturedarticle',
            name='issue',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_articles', to='magazine.MagazineIssue'),
        ),
    ]
