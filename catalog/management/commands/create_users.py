from django.core.management.base import BaseCommand, CommandError
from catalog.models import Users
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()
list_1 = []


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('arg_1', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        for _ in range(options['arg_1']):
            fake_name = fake.first_name()
            fake_last_name = fake.last_name()
            User.objects.bulk_create([User(first_name=fake_name,
                                           email=f'{fake_name}.{fake_last_name}@{fake.domain_name()}',
                                           password=fake.password(),
                                           last_name=fake_last_name,
                                           username=f'{fake_name}.{fake_last_name}')])
