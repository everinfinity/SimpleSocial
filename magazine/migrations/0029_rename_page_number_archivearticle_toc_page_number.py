# Generated by Django 3.2.2 on 2021-05-26 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0028_auto_20210526_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archivearticle',
            old_name='page_number',
            new_name='toc_page_number',
        ),
    ]
