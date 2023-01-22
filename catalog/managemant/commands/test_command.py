from django.core.management.base import BaseCommand, CommandError
from catalog.models import Users
from faker import Faker
fake = Faker
list_1 = []


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('arg_1', nargs='+', type=int, choices=range(1, 11))

    def handle(self, *args, **options):

        for el in range(options['arg_1']):
            Users.objects.create(name=fake.name, email=fake.email, password=fake.password)
