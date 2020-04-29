import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models
from reviews import models as reviews_models


class Command(BaseCommand):

    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_rooms = room_models.Room.objects.all()
        seeder.add_entity(
            reviews_models.Review,
            number,
            {
                # "review": lambda x: seeder.faker.address(),
                "accuracy": lambda x: random.randint(1, 6),
                "communication": lambda x: random.randint(1, 6),
                "cleanline": lambda x: random.randint(1, 6),
                "location": lambda x: random.randint(1, 6),
                "check_in": lambda x: random.randint(1, 6),
                "value": lambda x: random.randint(1, 6),
                "name": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(all_rooms),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
