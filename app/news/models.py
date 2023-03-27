from datetime import date

from django.db import models
from wagtail import blocks as wagtail_blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from blocks.blocks import (
    FormattedImageChooserStructBlock,
    HeadingBlock,
    PullQuoteBlock,
    SpacerBlock,
)


class NewsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    parent_page_types = [
        "home.HomePage",
    ]
    subpage_types = [
        "NewsTopicIndexPage",
        "NewsTypeIndexPage",
        "NewsItem",
    ]
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        return context


class NewsTopicIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    parent_page_types = [
        "NewsIndexPage",
    ]
    subpage_types = [
        "NewsTopic",
    ]
    max_count = 1


class NewsTopic(Page):
    intro = RichTextField(blank=True)

    content_panels = [
        FieldPanel("title"),
        FieldPanel("intro"),
    ]

    # Hide the settings panels
    settings_panels = []

    parent_page_types = [
        "NewsTopicIndexPage",
    ]
    subpage_types = []


class NewsTypeIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    parent_page_types = [
        "NewsIndexPage",
    ]
    subpage_types = [
        "NewsType",
    ]
    max_count = 1


class NewsType(Page):
    intro = RichTextField(blank=True)

    content_panels = [
        FieldPanel("title"),
        FieldPanel("intro"),
    ]

    # Hide the settings panels
    settings_panels = []

    parent_page_types = [
        "NewsTypeIndexPage",
    ]
    subpage_types = []


class NewsItem(Page):
    teaser = models.TextField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Briefly summarize the news item for display in news lists",
    )
    body = StreamField(
        [
            ("heading", HeadingBlock()),
            (
                "rich_text",
                wagtail_blocks.RichTextBlock(
                    features=[
                        "bold",
                        "italic",
                        "ol",
                        "ul",
                        "hr",
                        "link",
                        "document-link",
                        "superscript",
                        "superscript",
                        "strikethrough",
                        "blockquote",
                    ]
                ),
            ),
            ("pullquote", PullQuoteBlock()),
            ("image", FormattedImageChooserStructBlock(classname="full title")),
            ("document", DocumentChooserBlock()),
            ("spacer", SpacerBlock()),
        ],
        use_json_field=True,
    )
    body_migrated = models.TextField(
        help_text="Used only for content from old Drupal website.",
        null=True,
        blank=True,
    )
    drupal_node_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    publication_date = models.DateField(default=date.today)

    news_topic = models.ForeignKey(
        NewsTopic,
        on_delete=models.PROTECT,
        related_name="news_items",
        null=True,
        blank=True,
    )
    news_type = models.ForeignKey(
        NewsType,
        on_delete=models.PROTECT,
        related_name="news_items",
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("teaser"),
        FieldPanel("body"),
        MultiFieldPanel(
            heading="Metadata",
            children=[
                FieldPanel("publication_date"),
                FieldPanel("news_topic"),
                FieldPanel("news_type"),
            ],
        ),
    ]

    parent_page_types = [
        "NewsIndexPage",
    ]
    subpage_types = []
