from .base import *


ALLOWED_HOSTS = []

STATIC_ROOT =  os.path.join(os.path.dirname(BASE_DIR), "static")

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