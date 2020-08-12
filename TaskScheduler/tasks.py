from celery import shared_task

from .settings import EMAIL_HOST_USER
from Scheduler.models import TaskTracker

@shared_task(bind=True,
             name='Send_Emails_Everyday',
             max_retries=3,
             soft_time_limit=20)
def send_mail_daily():
    pass