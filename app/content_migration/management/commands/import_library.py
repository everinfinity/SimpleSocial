from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import all Library content"

    def add_arguments(self, parser):
        parser.add_argument("--data-directory", action="store", type=str)

    def handle(self, *args, **options):
        directory = options["data_directory"]

        if not directory.endswith("/"):
            directory += "/"

        library_items_filename = "library_items.csv"

        call_command(
            "import_library_item_facets",
            folder=f"{ directory }",
        )
        call_command(
            "import_library_items",
            file=f"{ directory }{ library_items_filename }",
        )
