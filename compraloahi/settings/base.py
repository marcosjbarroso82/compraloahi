import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SECRET_KEY = 'a#)y^h-f23l!*90%f+d8m(ld0rm-5)#c#9kit$bvocbrfen@l8'

STATIC_URL = '/static/'

# Defined django applications
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.comments',
)

# Defined third party applications
THIRD_PARTY_APPS = (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'bootstrap3',
    'taggit',
    'sorl.thumbnail',
    'django_comments_xtd', # Need packages: django.contrib.comments
    'haystack',
    'ckeditor',
    'postman',
    'rest_framework',
    'favit',
    'corsheaders',
    'rest_framework.authtoken',
)

# Defined own applications
LOCAL_APPS = (
    'apps.ad',
    'apps.adLocation',
    'apps.userProfile',
    'apps.user',
    'apps.message',
    'apps.common_tags',
    'apps.comment_notification',
)

# All aplication
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.userProfile.middleware.ValidProfileCreatedMiddleware',

)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)


ROOT_URLCONF = 'compraloahi.urls'

WSGI_APPLICATION = 'compraloahi.wsgi.application'



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# configuration urls for login
LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'


# Defined folder of static files to projects
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

# Nose
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Defined folder of media files to project
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

MEDIA_URL = "/media/"


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    "django.contrib.auth.context_processors.auth",
    # Required by allauth template tags
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    "postman.context_processors.inbox",

)


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)


THUMBNAIL_DEBUG = True
THUMBNAIL_FORMAT = 'PNG'


SITE_ID = 1

#SOCIALACCOUNT_QUERY_EMAIL = True

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],

        # Instead of OAuth
        #'METHOD': 'js_sdk'  # instead of 'oauth2'

        # Instead of Facebook Connect Javascript SDK
        'METHOD': 'oauth2'
    },
    'google': {
        'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
        'AUTH_PARAMS': {'access_type': 'online'}}
}

POSTMAN_DISALLOW_ANONYMOUS = True  # default is False
POSTMAN_DISALLOW_MULTIRECIPIENTS = True  # default is False
POSTMAN_DISALLOW_COPIES_ON_REPLY = True  # default is False
POSTMAN_DISABLE_USER_EMAILING = True  # default is False
# POSTMAN_AUTO_MODERATE_AS = True  # default is None
# POSTMAN_SHOW_USER_AS = 'get_full_name'  # default is None
# POSTMAN_QUICKREPLY_QUOTE_BODY = True  # default is False
POSTMAN_NOTIFIER_APP = None  # default is 'notification'
POSTMAN_MAILER_APP = None  # default is 'mailer'
# POSTMAN_AUTOCOMPLETER_APP = {
    # 'name': '',  # default is 'ajax_select'
    # 'field': '',  # default is 'AutoCompleteField'
    # 'arg_name': '',  # default is 'channel'
    # 'arg_default': 'postman_friends',  # no default, mandatory to enable the feature
# }  # default is {}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# Defined custom functionality to ckeditor
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': [
                    ["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker", 'TextColor'],
                    ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
                        'JustifyRight', 'JustifyBlock'],
                    ["Table", "Link", "Unlink", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'],
                    ["Maximize"]
                ],
        "removePlugins": "stylesheetparser",
        'uiColor' : '#f5f5f6',
        'with': '100%'
    },
}

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

# Config email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'testnubiquo@gmail.com'
EMAIL_HOST_PASSWORD = 'nubiquo1234567890'
EMAIL_USE_TLS = True


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)

}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
