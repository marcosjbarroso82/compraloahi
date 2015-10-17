import os

BASE_DIR =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


SECRET_KEY = '+^oi#xsco!d6_vy3+rlz16ua=hg&9p0j)-vl)_et0w)5gbfosl'

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
)

LOCAL_APPS = (
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
    'apps.report_error'
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


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
            os.path.join(BASE_DIR, "templates"),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Defined folder of static files to projects
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )


# Defined folder of media files to project
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

MEDIA_URL = "/media/"


LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'

#SOCIALACCOUNT_QUERY_EMAIL = True

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'public_profile'],

        # Instead of OAuth
        #'METHOD': 'js_sdk'  # instead of 'oauth2'

        # Instead of Facebook Connect Javascript SDK
        'METHOD': 'oauth2'
    },
    'google': {
        'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
        'AUTH_PARAMS': {'access_type': 'online'}}
}

SOCIALACCOUNT_EMAIL_VERIFICATION=True
"""
ACCOUNT_EMAIL_REQUIRED=False
ACCOUNT_CONFIRM_EMAIL_ON_GET=False
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL =  False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
"""


SITE_ID = 1
SITE_URL = "http://www.compraloahi.com.ar/"

DEFAULT_FROM_EMAIL = 'notification@compraloahi.com.ar'

EMAIL_BACKEND="djmail.backends.async.EmailBackend"
DJMAIL_REAL_BACKEND="django.core.mail.backends.smtp.EmailBackend"

# Config email
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = '1j3uUk9X82g8d7imFgcFRgqV3'
EMAIL_USE_TLS = True


THUMBNAIL_DEBUG = True
THUMBNAIL_FORMAT = 'PNG'


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


PUSH_NOTIFICATIONS_SETTINGS = {
        "GCM_API_KEY": "AIzaSyA_KurD4JmJdMSj12Mh0ZhjAI-LDJlNybI", #"AIzaSyD-750iceKvjKVno9p1Z4W6guATHMPJoak",
        #"APNS_CERTIFICATE": "/path/to/your/certificate.pem",
}
GCM_POST_URL = 'https://android.googleapis.com/gcm/send'

MSG_RELATED_APP_LABEL = 'app.ad'
MSG_RELATED_MODEL = 'Ad'
MSG_RELATED_OBJ_ID = 'pk'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

#HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_APP = "django_comments_xtd"
COMMENTS_XTD_CONFIRM_EMAIL = False


