# Generated by Django 3.2.12 on 2022-03-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20211117_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='drupal_node_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
