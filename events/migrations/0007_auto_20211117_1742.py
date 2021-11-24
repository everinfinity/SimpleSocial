# Generated by Django 3.2.8 on 2021-11-17 17:42

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.AlterField(
            model_name='event',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('width', wagtail.core.blocks.IntegerBlock(help_text='Enter the desired image width value in pixels up to 800 max.', max_value=800, min_value=0))]))], blank=True, null=True),
        ),
    ]
