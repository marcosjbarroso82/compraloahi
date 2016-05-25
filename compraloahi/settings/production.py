from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["*"]

STATIC_ROOT =  os.path.join(os.path.dirname(BASE_DIR), "static")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'compraloahi',
        'USER': 'm',
        'PASSWORD': 'camaleon',
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
        'task': 'compraloahi.tasks.backup',
        # 'schedule': timedelta(seconds=5),
        'schedule': crontab(minute=0, hour=0),

    },
    'backup_profile_media': {
        'task': 'compraloahi.tasks.backup_profile_media',
        # 'schedule': timedelta(seconds=5),
        'schedule': crontab(minute=0, hour=0),
    },
    'backup_ad_media': {
        'task': 'compraloahi.tasks.backup_ad_media',
        # 'schedule': timedelta(seconds=5),
        'schedule': crontab(minute=0, hour=0),
    },
    'update_index': {
        'task': 'compraloahi.tasks.update_index',
        'schedule': timedelta(hours=1),
    },

}
CELERY_TIMEZONE = 'UTC'
