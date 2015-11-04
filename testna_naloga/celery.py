from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testna_naloga.settings')

app = Celery('tasks')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.config_from_object('django.conf.settings')