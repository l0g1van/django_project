from django.core.management.base import BaseCommand

import catalog.models
from catalog.models import Users
from django.contrib.auth.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('arg_1', nargs='+', type=int)

    def handle(self, *args, **options):
        q = User.objects.filter(id__in=options['arg_1'])
        if q.filter(is_superuser=True).exists():
            self.stdout.write(self.style.SUCCESS('There is one or more superusers so I cant delete this items'))
        else:
            q.delete()
            self.stdout.write(self.style.SUCCESS('Items was successfully deleted'))
