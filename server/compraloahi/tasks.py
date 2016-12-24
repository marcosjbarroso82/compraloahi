from __future__ import absolute_import
# from .celery import app
from compraloahi.celery import app
from celery import shared_task
import subprocess
#import datetime
#from django.conf import settings


# @app.task
# @shared_task
# def backup():
#     cmd = "pg_dump -U " + settings.DATABASES['default']['USER'] + " " + settings.DATABASES['default']['NAME'] + " -f " + settings.BACKUP_FOLDER  + "/bkp-" + datetime.datetime.now().strftime("%y-%m-%d-%H:%M:%S") + ".sql"
#     # print(cmd)
#     r = subprocess.call(cmd, shell=True)
#
# @app.task
# @shared_task
# def backup_profile_media():
#     cmd = "tar -czvf " + settings.BACKUP_FOLDER  + "/media/profile/profile-" \
#           + datetime.datetime.now().strftime("%y-%m-%d-%H:%M:%S") + ".tgz " \
#           + "--directory=" + settings.MEDIA_ROOT + " profile"
#     r = subprocess.call(cmd, shell=True)
#
# @app.task
# @shared_task
# def backup_ad_media():
#     cmd = "tar -czvf " + settings.BACKUP_FOLDER  + "/media/ad/ad-" \
#           + datetime.datetime.now().strftime("%y-%m-%d-%H:%M:%S") + ".tgz " \
#           + "--directory=" + settings.MEDIA_ROOT + " ad"
#     r = subprocess.call(cmd, shell=True)


@app.task(bind=True)
@shared_task
def update_index():
    cmd = "./manage.py update_index --remove"
    r = subprocess.call(cmd, shell=True)

