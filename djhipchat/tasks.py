from __future__ import absolute_import, unicode_literals

from celery.task import task

from . import send_message as send_message_sync


@task(ignore_result=True)
def send_message(*args, **kwargs):
    return send_message_sync(*args, **kwargs)
