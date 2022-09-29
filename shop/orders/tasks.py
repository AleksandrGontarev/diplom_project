import os
from celery import shared_task
from django.core.mail import send_mail
import requests
import json
from orders.models import Order
from django.core import serializers


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
def get_order():

    orders_all = Order.objects.filter(status='Ordered')

    data = serializers.serialize('json', orders_all)

    try:
        url = "http://warehouse:8000/api/orders/"
        token = os.environ.get('TOKEN_SECRET')
        headers = {"content-type": "application/json; charset=UTF-8", 'Authorization': 'Token {}'.format(token)}
        response = requests.post(url, data=data, headers=headers)
        print("Status Code", response.status_code)
        print("JSON Response ", response.json())

        print("|||||||||||||||||||||||||||||||||||")
    except Exception as e:
        print(e)


