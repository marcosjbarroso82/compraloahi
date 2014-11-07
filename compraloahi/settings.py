import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'a#)y^h-f23l!*90%f+d8m(ld0rm-5)#c#9kit$bvocbrfen@l8'

DEBUG = True

TEMPLATE_DEBUG = True

STATIC_URL = '/static/'

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'bootstrap3',
    'taggit',
    'ad',
    'adLocation',
    'sorl.thumbnail',
    'userProfile',
    'ckeditor',
    'postman',
    'pagination',
    'django.contrib.comments',
    'django_comments_xtd',
    'haystack',
    'common_tags',
    'user',
    'message',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'compraloahi.urls'

WSGI_APPLICATION = 'compraloahi.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# configuration urls for login
LOGIN_URL = '/admin/login'
LOGIN_REDIRECT_URL = '/'



STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

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

# Dinamic theme change
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    "theme_manager.theme_manager.css_folder",
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
HAYSTACK_SIGNAL_PROCESSOR = 'ad.signals.RealtimeSignalProcessor'

COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_APP = "django_comments_xtd"


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'testnubiquo@gmail.com'
EMAIL_HOST_PASSWORD = 'nubiquo1234567890'
EMAIL_USE_TLS = True

