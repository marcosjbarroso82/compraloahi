from .base import *

DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = '/ system dir static folder/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

MEDIA_URL = "/media/"

