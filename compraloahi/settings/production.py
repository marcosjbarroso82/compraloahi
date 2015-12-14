from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["*"]

STATIC_ROOT =  os.path.join(os.path.dirname(BASE_DIR), "static")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_compraloahi',
        'USER': 'compraloahi',
        'PASSWORD': 'TRuP9y8abxQ0SmsfdT3AM7gLVn4GFuMaYhPV1HfZolOoZEVAgPemIQlN4Gd0zvf',
        'HOST': 'localhost',
        'PORT': '',
    }
}

from celery.schedules import crontab
from datetime import timedelta
# import djcelery
# djcelery.setup_loader()

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.join(os.path.dirname(__file__), '../..')))
BACKUP_FOLDER = os.path.join(PROJECT_ROOT, 'backups')

CELERYBEAT_SCHEDULE = {
    'backup': {
        # 'task': 'tasks.debug_task',
        'task': 'compraloahi.tasks.backup',
        # 'task': 'compraloahi.celery.debug_task',
        # 'schedule': timedelta(seconds=5),
        'schedule': crontab(minute=0, hour=0),

    },
    'backup_profile_media': {
        # 'task': 'tasks.debug_task',
        'task': 'compraloahi.tasks.backup_profile_media',
        # 'task': 'compraloahi.celery.debug_task',
        # 'schedule': timedelta(seconds=5),
        'schedule': crontab(minute=0, hour=0),
    },
    'backup_ad_media': {
        # 'task': 'tasks.debug_task',
        'task': 'compraloahi.tasks.backup_ad_media',
        # 'task': 'compraloahi.celery.debug_task',
        # 'schedule': timedelta(seconds=5),
        'schedule': crontab(minute=0, hour=0),
    },

}
CELERY_TIMEZONE = 'UTC'