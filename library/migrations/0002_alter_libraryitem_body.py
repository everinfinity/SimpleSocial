# Generated by Django 3.2.13 on 2022-05-11 10:40

import re

import django.core.validators
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
from django.db import migrations

import blocks.blocks
import documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="libraryitem",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    ("paragraph", wagtail.core.blocks.RichTextBlock()),
                    (
                        "image",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "width",
                                    wagtail.core.blocks.IntegerBlock(
                                        help_text="Enter the desired image width value in pixels up to 800 max.",
                                        max_value=800,
                                        min_value=0,
                                    ),
                                ),
                            ],
                            classname="full title",
                        ),
                    ),
                    ("document", documents.blocks.DocumentEmbedBlock()),
                    ("media", blocks.blocks.MediaBlock(icon="media")),
                    ("embed", wagtail.embeds.blocks.EmbedBlock()),
                    ("url", wagtail.core.blocks.URLBlock()),
                    ("quote", wagtail.core.blocks.BlockQuoteBlock()),
                    (
                        "target",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "target_slug",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Used to link to a specific location within this page. Slug should only contain letters, numbers, underscore (_), or hyphen (-).",
                                        validators=(
                                            django.core.validators.RegexValidator(
                                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                                "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                                                "invalid",
                                            ),
                                        ),
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
