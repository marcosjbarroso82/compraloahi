from __future__ import absolute_import
from .celery import app
from celery import shared_task
import subprocess
import datetime
from django.conf import settings


@app.task
@shared_task
def backup():
    cmd = "pg_dump -U " + settings.DATABASES['default']['USER'] + " " + settings.DATABASES['default']['NAME'] + " -f " + settings.BACKUP_FOLDER  + "/bkp-" + datetime.datetime.now().strftime("%y-%m-%d-%H-%M") + ".sql"
    print(cmd)
    r = subprocess.call(cmd, shell=True)