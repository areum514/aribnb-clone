from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument(
            "-t", "--times", default=1, type=int,
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, times):
            self.stdout.write(self.style.ERROR("love you"))
            self.stdout.write(self.style.SUCCESS("love you"))
