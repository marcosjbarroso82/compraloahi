from .base import *


ALLOWED_HOSTS = []


#STATIC_ROOT = '/opt/compraloahi/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_compraloahi',
        'USER': 'compraloahi',
        'PASSWORD': 'laserjet_1',
        'HOST': 'localhost',
        'PORT': '',
    }
}