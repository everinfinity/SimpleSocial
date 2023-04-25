import numpy as np
import pandas as pd
from django.core.management.base import BaseCommand
from tqdm import tqdm

from facets.models import (  # TODO: make sure to add library item topics
    Audience,
    Genre,
    Medium,
    TimePeriod,
)
from library.models import (
    LibraryIndexPage,
    LibraryItem,
    LibraryItemAuthor,
)

from .shared import (
    get_existing_magazine_author_from_db,
)


def add_library_item_authors(
    library_item,
    drupal_author_ids,
):
    drupal_author_ids_int = [
        int(author_id) for author_id in drupal_author_ids.split(", ")
    ]

    for drupal_author_id in drupal_author_ids_int:
        author = get_existing_magazine_author_from_db(drupal_author_id)

        if author:
            library_item_author_exists = LibraryItemAuthor.objects.filter(
                library_item=library_item,
                author=author,
            ).exists()

            if not library_item_author_exists:
                item_author = LibraryItemAuthor(
                    library_item=library_item,
                    author=author,
                )

                library_item.authors.add(item_author)


def add_library_item_keywords(library_item, keywords):
    for keyword in keywords.split(", "):
        library_item.tags.add(keyword)


class Command(BaseCommand):
    help = "Import all library items"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            action="store",
            type=str,
        )

    def handle(self, *args, **options):
        # Get the only instance of Magazine Department Index Page
        library_item_index_page = LibraryIndexPage.objects.get()

        library_items = (
            pd.read_csv(options["file"]).replace({np.nan: None}).to_dict("records")
        )

        for import_library_item in tqdm(
            library_items,
            desc="Library items",
            unit="row",
        ):
            library_item_exists = LibraryItem.objects.filter(
                drupal_node_id=import_library_item["node_id"]
            ).exists()

            if library_item_exists:
                library_item = LibraryItem.objects.get(
                    drupal_node_id=import_library_item["node_id"]
                )
            else:
                library_item = LibraryItem(
                    title=import_library_item["title"],
                    drupal_node_id=import_library_item["node_id"],
                )

                # Add library item to library branch of content tree
                library_item_index_page.add_child(instance=library_item)

                library_item_index_page.save()

            library_item.title = import_library_item["title"]
            library_item.description = import_library_item["Description"]

            # # TODO: Remember to uncomment this line when done
            # # developing the remaining import script
            # # library_item.body = parse_media_blocks(import_library_item["Media"])
            library_item.body = None

            if import_library_item["Audience"] is not None:
                library_item.item_audience = Audience.objects.get(
                    title=import_library_item["Audience"]
                )

            if import_library_item["Genre"] is not None:
                library_item.item_genre = Genre.objects.get(
                    title=import_library_item["Genre"]
                )

            if import_library_item["Medium"] is not None:
                library_item.item_medium = Medium.objects.get(
                    title=import_library_item["Medium"]
                )

            if import_library_item["Time Period"] is not None:
                library_item.item_time_period = TimePeriod.objects.get(
                    title=import_library_item["Time Period"]
                )

            # Authors
            if import_library_item["drupal_magazine_author_ids"] is not None:
                add_library_item_authors(
                    library_item,
                    import_library_item["drupal_magazine_author_ids"],
                )

            # - Keywords
            if import_library_item["Keywords"] is not None:
                add_library_item_keywords(
                    library_item,
                    import_library_item["Keywords"],
                )

            # Website
            if import_library_item["Website"] is not None:
                url_stream_block = (
                    "url",
                    import_library_item["Website"],
                )

                library_item.body.append(url_stream_block)

            library_item.save()
