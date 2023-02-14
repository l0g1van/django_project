from django.core.mail import send_mail

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

