from celery import shared_task
from django.core.mail import send_mail
from orders.models import Order


@shared_task
def send(email, text_reminder):
    send_mail(
        'Reminder',
        text_reminder,
        'gontarevsanya@example.com',
        [email, ],
        fail_silently=False,
    )


@shared_task
def chek_order():
    orders_all = Order.objects.filter(status='Success')
    for i in orders_all:
        email = i.user_email
        text_reminder = 'Order confirm !!!'
        send(email=email, text_reminder=text_reminder)
