import random
from faker import Faker
from django.core.management.base import BaseCommand
from catalog.models import Author, Book

fake = Faker()


class Command(BaseCommand):

    def handle(self, *args, **options):
        Author.objects.all().delete()
        Book.objects.all().delete()

        authors = [Author(name=f"Author{index}", age=random.randint(20, 100)) for index in range(1, 250)]
        Author.objects.bulk_create(authors)

        counter = 0
        books = []
        for author in Author.objects.all():
            for i in range(5):
                counter = counter + 1
                books.append(Book(name=f"Book{counter}", price=random.randint(50, 300), authors=author,
                                  pages=random.randint(150, 250), rating=random.randint(1, 10), pubdate=fake.date()))

        Book.objects.bulk_create(books)
