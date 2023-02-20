import requests
from bs4 import BeautifulSoup

from django.core.mail import send_mail

from catalog.models import AuthorAndQuote

from celery import shared_task


@shared_task()
def send_email_task(email_address, message):
    send_mail(
        'Your email',
        message,
        'from@example.com',
        [email_address],
        fail_silently=False
    )


@shared_task()
def quotes_add():
    list_1 = list()
    for page in range(11):
        r = requests.get(f'https://quotes.toscrape.com/page/{page}/')
        soup = BeautifulSoup(r.content, features="html.parser")
        quotes = soup.find_all("div", {"class": "quote"})
        for quote in quotes:
            if len(list_1) < 5:
                if not AuthorAndQuote.objects.filter(quote=quote.find('span', {'class': 'text'}).text).exists():
                    quote_text = quote.find('span', {'class': 'text'}).text
                    author_name = quote.find('small', {'class': 'author'}).text
                    author_link = quote.find('a')['href']
                    link = f"https://quotes.toscrape.com{author_link}"
                    rp = requests.get(link)
                    if rp.status_code == 200:
                        soup_2 = BeautifulSoup(rp.content, features="html.parser")
                        birth_date = soup_2.find('span', {'class': 'author-born-date'}).text
                        author_details = ' '.join(soup_2.find('div', {'class': 'author-description'}).text.split())
                        list_1.append([quote_text, author_name, author_details, birth_date])
                        # print(list_1)
            else:
                break
    if list_1:
        for el in list_1:
            AuthorAndQuote.objects.create(name=el[1], details=el[2], birth_date=el[3], quote=el[0])
    else:
        send_mail(
            'Your email',
            'There are no more new quotes',
            'from@example.com',
            'myemail@example.com',
            fail_silently=False
        )
