from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerytask.settings')
app = Celery('celeryapp', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Looks up for task module in Django applications and loads them
app.autodiscover_tasks()
