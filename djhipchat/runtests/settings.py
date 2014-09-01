from __future__ import absolute_import
import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
ROOT_URLCONF = 'djhipchat.runtests.urls'

BROKER_URL = 'amqp://guest:guest@localhost//'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']

SECRET_KEY = 'not a secret'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'djhipchat',
]

# Clear a warning on Django 1.7
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

DJHIPCHAT_CELERY_TESTS = bool(os.environ.get('ENABLE_CELERY_TESTS', False))
if DJHIPCHAT_CELERY_TESTS:
    INSTALLED_APPS += ['djcelery']
    import djcelery
    djcelery.setup_loader()
