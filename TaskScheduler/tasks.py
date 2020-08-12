from celery import shared_task

from .settings import EMAIL_HOST_USER
from Scheduler.models import TaskTracker
from django.core.mail import send_mail
#from time import sleep
# @shared_task
# def send_email_task():
#     """
#     This was a trial Task
#     """
#     sleep(10)
#     send_mail(subject="yooo",message="Hello World!",recipient_list=["asatwe@gmail.com"])
#     return None


@shared_task(bind=True,
             name='Send_Emails_Everyday',
             max_retries=3,
             soft_time_limit=20)
def send_mail_daily():
    trackers=TaskTracker.objects.filter(update_type="daily")

    for tracker in trackers:
        subject=f"Daily Email for task type {tracker.task_type}"
        text=f"This is an Daily Update Email for the task type {tracker.task_type}. Description for the same is {tracker.task_desc}"
        send_mail(subject=subject,message=text,recipient_list=[tracker.email],fail_silently=False)

@shared_task(bind=True,
             name='Send_Emails_Weekly',
             max_retries=3,
             soft_time_limit=20)
def send_mail_weekly():
    trackers=TaskTracker.objects.filter(update_type="weekly")

    for tracker in trackers:
        subject=f"Weekly Email for task type {tracker.task_type}"
        text=f"This is a Weekly Update Email for the task type {tracker.task_type}. Description for the same is {tracker.task_desc}"
        send_mail(subject=subject,message=text,recipient_list=[tracker.email],fail_silently=False)




@shared_task(bind=True,
             name='Send_Emails_Monthly',
             max_retries=3,
             soft_time_limit=20)
def send_mail_monthly():
    trackers=TaskTracker.objects.filter(update_type="monthly")

    for tracker in trackers:
        subject=f"Monthly Email for task type {tracker.task_type}"
        text=f"This is a monthly Update Email for the task type {tracker.task_type}. Description for the same is {tracker.task_desc}"
        send_mail(subject=subject,message=text,recipient_list=[tracker.email],fail_silently=False)
