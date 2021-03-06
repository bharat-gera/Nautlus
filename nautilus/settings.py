"""
Django settings for nautilus project.

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
SECRET_KEY = '*wlz9^k!o%f=$nob!)ocih&-z9i-mzz!m*^%o7zx1lka#0kj6c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'kombu.transport.django',
    'rest_framework.authtoken',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework_gis',
    'search',
    'person',
    'djcelery',
    'workers',
    'accounts',
    'uploadimages',
    'feedback',
    'places',
    'local',
    'wallet',
    'order',
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

ROOT_URLCONF = 'nautilus.urls'

WSGI_APPLICATION = 'nautilus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'nautilus',
        'USER': 'nautilusadmin',
        'PASSWORD':'nautilus',	
        'HOST':'localhost'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
)


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'person.Person'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

POSTGIS_VERSION = (2, 0, 3)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
     )

# Project settings

STATICFILES_DIRS = (os.path.join(BASE_DIR, "staticfiles"),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

GOOGLE_NEAR_BY = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

#GOOGLE_API_KEY = 'AIzaSyAf_BlBBXCZEUrg_a1Df3zuWuQji4gKyxU'
GOOGLE_API_KEY = 'AIzaSyAPl1zoa3IZw1XXR01WMOHpBxy2U0G7_vs'          #Arya's Api

GOOGLE_DETAIL_API = 'https://maps.googleapis.com/maps/api/place/details/json?'

GOOGLE_AUTO_API = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?'

GOOGLE_PHOTO_API = 'https://maps.googleapis.com/maps/api/place/photo?'

NEAR_BY_RADIUS = 50000   #in meters

SWAGGER_SETTINGS = {
    "exclude_namespaces": [],  # List URL namespaces to ignore
    "api_version": '0.6',  # Specify your API's version
    "api_path": "/",  # Specify the path to your API not a root level
    "enabled_methods": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    "api_key": '',  # An API key
    "is_authenticated": False,  # Set to True to enforce user authentication,
    "is_superuser": False,  # Set to True to enforce admin only access0
}

# Rest Framework Settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework.authentication.BasicAuthentication',
#        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
#         'rest_framework_csv.renderers.CSVRenderer',
        ),
}


PROFILE_URL = 'accounts/profile'
DEFAULT_DISTANCE = 50000               #in meters
MIN_REVIEW_LENGTH = 120                #JUST A LENGTH IN NUMBER
MAX_REVIEW_LENGTH = 240
CHAR_PRICE = 2              #in paisa  
ONE_POINT_CHARS = 40       # 1point=40characters
LEVEL_UP = 15               # 15 points level up
LEVEL_UP_BONUS = 50    #in rs

