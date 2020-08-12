from __future__ import absolute_import, unicode_literals

import os
from dotenv import load_dotenv
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskScheduler.settings')

app = Celery('TaskScheduler')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.conf.broker_url=os.getenv("CELERY_URI")
app.conf.update(result_expires=3600,enable_utc=True,timezone='Asia/Kolkata')

app.conf.beat_schedule={
    "every day at 5 PM":{
        "task":"Send_Emails_Everyday",
        "schedule":crontab(hour=17,minute=0)
    },
    "every week on Monday":{
        "task":"Send_Emails_Weekly",
        "schedule":crontab(minute=0,hour=0,day_of_week="monday")
    },
    "every first day of Month":{
        "task":"Send_Emails_Monthly",
        "schedule":crontab(minute=0,hour=0,day_of_month=1)
    }
}
app.autodiscover_tasks(settings.INSTALLED_APPS)