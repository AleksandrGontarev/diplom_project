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
def get_count():
    try:
        url = "http://warehouse:8000/api/books/"
        token = os.environ.get('TOKEN_SECRET')
        response = requests.get(url, headers={'Authorization': 'Token ' + token})
        parsed = response.json()
        print('***************************')
        print(parsed['count'])
        # add cod ###########################################
    except Exception as e:
        print(e)
