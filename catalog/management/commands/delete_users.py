from django.core.management.base import BaseCommand

import catalog.models
from catalog.models import Users


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('arg_1', nargs='+', type=int)

    def handle(self, *args, **options):
        try:
            for el in options['arg_1']:
                if Users.objects.filter(id=el).get() not in Users.objects.filter(superuser=1):
                    Users.objects.filter(id=el, superuser=0).delete()
                    self.stdout.write(self.style.SUCCESS(f'output: {Users.objects.filter(id=el, superuser=0).get()}'))
                else:
                    self.stdout.write(self.style.SUCCESS('There is one or more superusers with that ids'))
        except catalog.models.Users.DoesNotExist:
            pass
