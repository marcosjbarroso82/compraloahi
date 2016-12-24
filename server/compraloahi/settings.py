from __future__ import absolute_import, unicode_literals

import os
import warnings


BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# Environment
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
if ENVIRONMENT == 'dev_local':
    DEVNAME = os.environ['DEVNAME']

DEBUG = ENVIRONMENT in ('dev_local', 'dev', 'test')
TEMPLATE_DEBUG = DEBUG


if not os.environ.get('SECRET_KEY'):
    warnings.warn((
                      "Please define SECRET_KEY before importing {0}, as a fallback "
                      "for when the environment variable is not available."
                  ).format(__name__))
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')


################## APPS CONFIG #############################

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

)

THIRD_PARTY_APPS = (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'bootstrap3',
    'taggit',
    'sorl.thumbnail',
    'django_comments',
    'django_comments_xtd', # Need packages: django.contrib.comments
    'haystack',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'push_notifications',
    'rest_auth',
    'rest_auth.registration',
    'djmail',
    'jsonify',
    'colorful',
    #'djcelery',
    #'termsandconditions',
)

LOCAL_APPS = (
    'compraloahi',
    'apps.common_tags',
    'apps.ad',
    'apps.adLocation',
    'apps.userProfile',
    'apps.user',
    'apps.notification',
    'apps.rating',
    'apps.msg',
    'apps.favorite',
    'apps.faq',
    'apps.report_error',
    'apps.util',
    'apps.interest_group',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

############## DATABASE CONFIG #############
# DATABASES = {}
#
# if 'DB_DEFAULT_URL' in os.environ:
#     import dj_database_url
#     if ENVIRONMENT:
#         DATABASES = {
#             'default': dj_database_url.parse(os.environ['DB_DEFAULT_URL'])
#         }

DATABASES = {
    'default': {
        'ENGINE': os.environ['DB_ENGINE'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}



MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'compraloahi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, "templates"),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                #"allauth.account.context_processors.account",
                #"allauth.socialaccount.context_processors.socialaccount"
            ],
            },
        },
    ]

WSGI_APPLICATION = 'compraloahi.wsgi.application'




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Defined folder of static files to projects
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

# Defined folder of media files to project
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


######### AUTHENTICATION CONFIG ################

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/panel/mis-avisos/'

#SOCIALACCOUNT_QUERY_EMAIL = True
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'public_profile'],
        'METHOD': 'oauth2'
    },
    'google': {
        'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
        'AUTH_PARAMS': {'access_type': 'online'}}
}

SOCIALACCOUNT_EMAIL_VERIFICATION=True

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = '/panel/mis-aviso/crear/'

"""
ACCOUNT_EMAIL_REQUIRED=False
ACCOUNT_CONFIRM_EMAIL_ON_GET=False
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL =  False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
"""


############ THUMB CONFIG ###############


THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_FORMAT = 'PNG'


###### REST FRAMEWORK CONFIG ######################

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'compraloahi.views.CustomPagination'

}




########### PUSH NOTIFICATIONS CONFIG ###############
PUSH_NOTIFICATIONS_SETTINGS = {
    "GCM_API_KEY": "AIzaSyA_KurD4JmJdMSj12Mh0ZhjAI-LDJlNybI", #"AIzaSyD-750iceKvjKVno9p1Z4W6guATHMPJoak",
    #"APNS_CERTIFICATE": "/path/to/your/certificate.pem",
}
GCM_POST_URL = 'https://android.googleapis.com/gcm/send'


########## MESSAGES APP CONFIG ###############
MSG_RELATED_APP_LABEL = 'app.ad'
MSG_RELATED_MODEL = 'Ad'
MSG_RELATED_OBJ_ID = 'pk'


########## HAYSTACK CONFIG #############
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://elasticsearch:9200/',
        'INDEX_NAME': 'haystack',
        },
    }

#HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10


######### COMMENT CONFIG ##################
COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_APP = "django_comments_xtd"
COMMENTS_XTD_CONFIRM_EMAIL = False


########## LOGGIN CONFIG ####################


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
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'compraloahi.log',
            'formatter': 'verbose'
        },
        'debug': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/compraloahi-debug.log',
            'formatter': 'verbose'
        },
        },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG' if DEBUG else 'INFO',
            },
        'debug': {
            'handlers': ['debug'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            },
        }
}


################ CONFIG SERVER ###########

# Trust our nginx server
USE_X_FORWARDED_HOST = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = os.environ.get('SITE_DOMAIN', '').split('|')
MY_SITE_DOMAIN = ALLOWED_HOSTS[0]
SITE_ID = 1
#SITE_URL = "http://www.compraloahi.com.ar/"
SITE_URL = '{0}://{1}'.format(os.environ.get('SITE_PROTOCOL', ''),
                              MY_SITE_DOMAIN)


###### CONFIG MEMCACHE #########

# Memcache
# try:
#     # pylint:disable=unused-import,import-error,wrong-import-position
#     import memcache
#     # pylint:enable=unused-import,import-error,wrong-import-position
#
#     CACHES = {
#         'default': {
#             'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#             'LOCATION': os.environ['MEMCACHE_HOSTS'].split('|'),
#             'KEY_PREFIX': os.environ['MEMCACHE_PREFIX'],
#         },
#     }
#
# except (ImportError, KeyError):
#     pass


############## CONFIG EMAIL BACKEND ###########

EMAIL_BACKEND="djmail.backends.async.EmailBackend"
DJMAIL_REAL_BACKEND="django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.zoho.com')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL', 'notificacion@compraloahi.com.ar')

EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS', 'laserjet1')
EMAIL_USE_TLS = True


##################### CONFIG CELERY TASK ###########

#from celery.schedules import crontab
from datetime import timedelta

#BACKUP_FOLDER = os.path.join(PROJECT_ROOT, 'backups')
BROKER_URL = "amqp://{user}:{password}@rabbitmq:5672//?heartbeat=30".format(
    user=os.environ.get('RABBITMQ_DEFAULT_USER'),
    password=os.environ.get('RABBITMQ_DEFAULT_PASS')
)

CELERYBEAT_SCHEDULE = {
    # 'backup': {
    #     'task': 'compraloahi.tasks.backup',
    #     # 'schedule': timedelta(seconds=5),
    #     'schedule': crontab(minute=0, hour=0),
    #
    # },
    # 'backup_profile_media': {
    #     'task': 'compraloahi.tasks.backup_profile_media',
    #     # 'schedule': timedelta(seconds=5),
    #     'schedule': crontab(minute=0, hour=0),
    # },
    # 'backup_ad_media': {
    #     'task': 'compraloahi.tasks.backup_ad_media',
    #     # 'schedule': timedelta(seconds=5),
    #     'schedule': crontab(minute=0, hour=0),
    # },
    'update_index': {
        'task': 'compraloahi.tasks.update_index',
        'schedule': timedelta(minutes=3),
        },

    }
CELERY_TIMEZONE = 'UTC'


################ ADMINS SITE ####

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS