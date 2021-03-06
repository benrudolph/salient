"""
Django settings for salient project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sum*%54oe=a0e2#ay9)msi!5_(+z8i3m&59w!g)i3s172&jqjd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = BASE_DIR + '/static/uploads/'

BOWER_COMPONENTS_ROOT = BASE_DIR + '/components/'

BOWER_INSTALLED_APPS = (
    'jquery#1.9',
    'underscore',
    'knockout',
    'sammy',
    'highcharts-release',
    'd3',
)

BROKER_URL = 'redis://localhost:6379/0'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
    BASE_DIR + '/core/templates/',
    BASE_DIR + '/analyzer/templates/',
    BASE_DIR + '/accounts/templates/',
    BASE_DIR + '/uploader/templates/',
    BASE_DIR + '/visualize/templates/',
)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'djangobower',
    'crispy_forms',
    'debug_toolbar',
    'bootstrap3',
    'accounts',
    'uploader',
    'analyzer',
    'salient',
    'rest_framework',
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

ROOT_URLCONF = 'salient.urls'

WSGI_APPLICATION = 'salient.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'salient',
        'USER': 'salient',
        'PASSWORD': 'salient',
        'HOST': 'localhost',
        'PORT': '',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BOWER_PATH = '/usr/local/bin/bower'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    "djangobower.finders.BowerFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

STATICFILES_DIRS = (
    BASE_DIR + '/core/static/',
    BASE_DIR + '/uploader/static/',
    BASE_DIR + '/visualize/static/',
    #BASE_DIR + '/analyzer/static/',
    #BASE_DIR + '/accounts/static/',
    os.path.join(BASE_DIR, "static"),
)
