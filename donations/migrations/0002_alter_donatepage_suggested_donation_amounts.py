# Generated by Django 4.1.1 on 2022-10-05 15:53

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("donations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donatepage",
            name="suggested_donation_amounts",
            field=wagtail.fields.StreamField(
                [
                    (
                        "suggested_donation_amounts",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "once",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.IntegerBlock(label="Amount")
                                    ),
                                ),
                                (
                                    "monthly",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.IntegerBlock(label="Amount")
                                    ),
                                ),
                                (
                                    "yearly",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.IntegerBlock(label="Amount")
                                    ),
                                ),
                            ],
                            max_num=1,
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
