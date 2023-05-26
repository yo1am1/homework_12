from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Publication

fake = Faker()


class Command(BaseCommand):
    help = "Generate random article(publication)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=1,
            help="Specific number of publications you want to generate",
        )

    def handle(self, *args, **options):
        if options["count"]:
            count = options["count"]
            for i in range(count):
                Teacher.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=fake.random_int(min=24, max=80),
                    email=fake.email(),
                )
            self.stdout.write(self.style.SUCCESS(f"Successfully generated!"))