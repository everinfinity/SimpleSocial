# Generated by Django 2.1.7 on 2019-05-12 01:57

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitypage',
            name='events_intro',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
