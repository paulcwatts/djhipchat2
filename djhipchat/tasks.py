from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from celery import shared_task
from djhipchat import get_backend


@shared_task(ignore_result=True)
def send_message(*args, **kwargs):
    try:
        backend = get_backend(getattr(settings, 'HIPCHAT_CELERY_BACKEND'))
    except AttributeError:
        raise ImproperlyConfigured(
            "You need to specify HIPCHAT_CELERY_BACKEND")

    backend.send_message(*args, **kwargs)
