from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class NewsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    parent_page_types = ["home.HomePage", ]
    subpage_types = []
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        return context


class NewsTopicsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    parent_page_types = ["NewsIndexPage", ]
    subpage_types = ["NewsTopic", ]
    max_count = 1


class NewsTopic(Page):
    content_panels = [FieldPanel("title")]

    # Hide the settings panels
    settings_panels = []

    parent_page_types = ["NewsTopicsIndexPage", ]
    subpage_types = []
