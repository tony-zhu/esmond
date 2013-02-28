import os
import os.path
from esxsnmp.config import get_config

# Django settings for ed project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TESTING = os.environ.get("ESXSNMP_TESTING", False)
ESXSNMP_CONF = os.environ.get("ESXSNMP_CONF")
ESXSNMP_ROOT = os.environ.get("ESXSNMP_ROOT")

if not ESXSNMP_ROOT:
    raise Error("ESXSNMP_ROOT not definied in environemnt")

if not ESXSNMP_CONF:
    ESXSNMP_CONF = os.path.join(ESXSNMP_ROOT, "esxsnmp.conf")

ESXSNMP_SETTINGS = get_config(ESXSNMP_CONF)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': ESXSNMP_SETTINGS.sql_db_engine,
        'NAME': ESXSNMP_SETTINGS.sql_db_name,
        'HOST': ESXSNMP_SETTINGS.sql_db_host,
        'USER': ESXSNMP_SETTINGS.sql_db_user,
        'PASSWORD': ESXSNMP_SETTINGS.sql_db_password,
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'America/Chicago'
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

STATIC_URL = '/static/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''


# Make this unique, and don't share it with anybody.
SECRET_KEY = '%!=ok&32r5%ztl*^zqkm5++j)3crj64rf$=v)1mb^2i*%6ob41'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'esxsnmp.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'esxsnmp.api',
    'esxsnmp.admin',
    'django.contrib.admin',
)
