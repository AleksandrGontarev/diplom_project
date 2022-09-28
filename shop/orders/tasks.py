import os
from celery import shared_task
from django.core.mail import send_mail
import requests
import json


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
    try:
        url = "http://warehouse:8000/api/orders/"
        token = os.environ.get('TOKEN_SECRET')
        response = requests.get(url, headers={'Authorization': 'Token ' + token})   # add method post
        parsed = response.json()
        print("|||||||||||||||||||||||||||||||||||")
        print(parsed['results'][0]['order_id_in_shop'])
        # add cod #############################################
    except Exception as e:
        print(e)
