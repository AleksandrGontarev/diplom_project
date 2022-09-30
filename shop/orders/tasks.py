import os
from celery import shared_task
from django.core.mail import send_mail
import requests
import json
from orders.models import Order, OrderItem
from django.core import serializers


@shared_task
def send(email, text_reminder):
    if text_reminder == 'ordered':
        send_mail(
            'Reminder',
            text_reminder,
            'gontarevsanya@example.com',
            [email, ],
            fail_silently=False,
        )


@shared_task
def get_order():
    token = os.environ.get('TOKEN_SECRET')
    headers = {'Authorization': 'Token {}'.format(token)}
    orders_all = Order.objects.filter(status='ordered')
    for order in orders_all:
        user = order.user_id.email
        request_obj = {
            "delivery_address": order.delivery_address,
            "status": "i",
            "user_email": user,
            "order_id_in_shop": order.pk,
        }

        try:
            url = "http://warehouse:8000/api/orders/"
            token = os.environ.get('TOKEN_SECRET')
            headers = {'Authorization': 'Token {}'.format(token)}
            check = requests.get(url, headers=headers)
            parsed = check.json()
            response = requests.post(url=url, json=request_obj, headers=headers)
            print("Status Code", response.status_code)
            print("JSON Response ", response.json())
        except Exception as e:
            print(e)

@shared_task
def get_order1():
    token = os.environ.get('TOKEN_SECRET')
    headers = {'Authorization': 'Token {}'.format(token)}
    order_id_all = OrderItem.objects.all()
    for i in order_id_all:
        order_item_all = {
            "quantity": i.quantity
        }

        try:
            url1 = "http://warehouse:8000/api/orderitems/"
            response1 = requests.post(url=url1, json=order_item_all, headers=headers)
            print("Status Code", response1.status_code)
            print("JSON Response ", response1.json())
        except Exception as e:
            print(e)



