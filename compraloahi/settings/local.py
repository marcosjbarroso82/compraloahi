from .base import *

ALLOWED_HOSTS = ['*']
DEBUG = True

TEMPLATE_DEBUG = True


INSTALLED_APPS = INSTALLED_APPS + (
    'django_extensions',   # for Ipython Notebook
    #'debug_toolbar',
)


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'compraloahi',
        'USER': 'postgres',
        'PASSWORD': 'laserjet1',
        'HOST': 'localhost',
        'PORT': '',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(filename)s][%(funcName)s][%(lineno)d][%(name)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'compraloahi.log',
            'formatter': 'verbose'
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/compraloahi-debug.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'debug': {
            'handlers': ['debug'],
            'level': 'DEBUG',
        },
    }
}

INTERNAL_IPS = ('127.0.0.1',)
