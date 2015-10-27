# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'd2pk0qfit7ksi5',
        'USER': 'lbyxuuzjtxkpjy',
        'PASSWORD':'aQXyHCPG7mke6XX-mjTBb-SA5Z',
        'HOST':'ec2-54-225-197-30.compute-1.amazonaws.com'
    }
}

DATABASES = {'default':dj_database_url.config()}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

