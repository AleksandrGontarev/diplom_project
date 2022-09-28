import os

from celery import Celery

from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     "get_count": {
#         "task": "books.tasks.get_count",
#         # "schedule": crontab(minute=0, hour="1-23/2"),
#         "schedule": crontab(minute="*/1")},
#     "get_order": {
#         "task": "orders.tasks.get_order",
#         # "schedule": crontab(minute=0, hour="1-23/2"),
#         "schedule": crontab(minute="*/1")},
# }


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
