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