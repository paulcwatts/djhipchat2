import sys
from django.conf import settings


APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'djhipchat',
]

try:
    import djcelery
    APPS += ['djcelery']
except ImportError:
    pass

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   CELERY_ALWAYS_EAGER=True,
                   CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                   ROOT_URLCONF='djhipchat.urls',
                   INSTALLED_APPS=APPS)

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['djhipchat', ])
if failures:
    sys.exit(failures)
