# Generated by Django 4.1.4 on 2022-12-30 13:50

import re

import django.core.validators
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks
from django.db import migrations

import blocks.blocks
import documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0013_alter_libraryitem_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="libraryitem",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading_level",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("h2", "Level 2 (child of level 1)"),
                                            ("h3", "Level 3 (child of level 2)"),
                                            ("h4", "Level 4 (child of level 3)"),
                                            ("h5", "Level 5 (child of level 4)"),
                                            ("h6", "Level 6 (child of level 5)"),
                                        ],
                                        help_text="These different heading levels help to communicate the organization and hierarchy of the content on a page.",
                                    ),
                                ),
                                (
                                    "heading_text",
                                    wagtail.blocks.CharBlock(
                                        help_text="The text to appear in the heading."
                                    ),
                                ),
                                (
                                    "target_slug",
                                    wagtail.blocks.CharBlock(
                                        help_text="Used to link to a specific location within this page. A slug should only contain letters, numbers, underscore (_), or hyphen (-).",
                                        required=False,
                                        validators=(
                                            django.core.validators.RegexValidator(
                                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                                "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                                                "invalid",
                                            ),
                                        ),
                                    ),
                                ),
                                (
                                    "color",
                                    wagtail_color_panel.blocks.NativeColorBlock(
                                        required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "rich_text",
                        wagtail.blocks.RichTextBlock(
                            features=[
                                "h2",
                                "h3",
                                "bold",
                                "italic",
                                "ol",
                                "ul",
                                "link",
                                "hr",
                            ]
                        ),
                    ),
                    (
                        "image",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "width",
                                    wagtail.blocks.IntegerBlock(
                                        help_text="Enter the desired image width value in pixels up to 800 max.",
                                        max_value=800,
                                        min_value=0,
                                    ),
                                ),
                                (
                                    "align",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[("left", "Left"), ("right", "Right")],
                                        help_test="Optionally align image left or right",
                                        icon="file-richtext",
                                        required=False,
                                    ),
                                ),
                            ],
                            classname="full title",
                        ),
                    ),
                    ("document", documents.blocks.DocumentEmbedBlock()),
                    ("media", blocks.blocks.MediaBlock(icon="media")),
                    ("embed", wagtail.embeds.blocks.EmbedBlock()),
                    ("url", blocks.blocks.WfURLBlock()),
                    ("quote", wagtail.blocks.BlockQuoteBlock()),
                    (
                        "spacer",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "height",
                                    wagtail.blocks.DecimalBlock(
                                        decimal_places=1,
                                        help_text="The height of this spacer in 'em' values where 1 em is one uppercase M.",
                                        min_value=0,
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
