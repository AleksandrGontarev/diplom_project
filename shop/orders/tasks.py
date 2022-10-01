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
        order_item_all = OrderItem.objects.filter(order_id=order.pk)
        order_list = []
        for j in order_item_all:
            order_item = {
                "quantity": j.quantity,
                "order_id": j.order_id,
                "book_id": j.book_id,
            }
            order_list.append(order_item)
        request_obj = {
            "delivery_address": order.delivery_address,
            "status": "i",
            "user_email": user,
            "order_id_in_shop": order.pk,
            "orderitem": [],
        }


        try:
            url = "http://warehouse:8000/api/orders/"
            token = os.environ.get('TOKEN_SECRET')
            headers = {'Authorization': 'Token {}'.format(token)}
            check = requests.get(url, headers=headers)
            parsed = check.json()
            if parsed["results"]:
                for j in parsed['results']:
                    if j["order_id_in_shop"] != order.pk:
                        response = requests.post(url=url, json=request_obj, headers=headers)
                        print("Status Code", response.status_code)
                        print("JSON Response ", response.json())
                        get_order1()
            else:
                response = requests.post(url=url, json=request_obj, headers=headers)
        except Exception as e:
            print(e)


@shared_task
def get_order1():
    token = os.environ.get('TOKEN_SECRET')
    headers = {'Authorization': 'Token {}'.format(token)}
    order_item_all = OrderItem.objects.all()
    for item in order_item_all:
        order_item_all = {
            "quantity": item.quantity,
            "order_id": item.order_id.pk,
            "book_id": str(item.book_id.id_in_store),
        }

        try:
            url1 = "http://warehouse:8000/api/orderitems/"
            # response1 = requests.post(url=url1, json=order_item_all, headers=headers)
            # print("Status Code", response1.status_code)
            # print("JSON Response ", response1.json())
        except Exception as e:
            print(e)
