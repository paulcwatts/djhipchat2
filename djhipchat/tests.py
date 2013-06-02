from __future__ import absolute_import, unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from django.test.utils import override_settings
from django.utils.unittest import skipUnless

import djhipchat
from djhipchat import get_backend

try:
    from djhipchat.tasks import send_message as send_message_task
except (ImportError, ImproperlyConfigured):
    send_message_task = None


def _backend(name):
    return 'djhipchat.backends.%s.HipChatBackend' % name


class BackendTest(TestCase):
    def test_backend_errors(self):
        self.assertRaises(ImproperlyConfigured,
                          lambda: get_backend('djhipchat.foo.BadModule'))
        self.assertRaises(ImproperlyConfigured,
                          lambda: get_backend(
                              'djhipchat.backends.dummy.BadClass'))

    @override_settings(HIPCHAT_BACKEND=_backend('dummy'))
    def test_dummy(self):
        backend = get_backend(_backend('dummy'))
        self.assertIsNotNone(backend)

        djhipchat.sent_messages = []
        djhipchat.send_message('1234', 'dummy')
        self.assertEqual([], djhipchat.sent_messages)

    @override_settings(HIPCHAT_BACKEND=_backend('locmem'))
    def test_locmem(self):
        backend = get_backend(_backend('locmem'))
        self.assertIsNotNone(backend)

        djhipchat.sent_messages = []
        djhipchat.send_message('1234', 'locmem test', sender='TestFrom')
        # (room_id, message, sender, message_format, notify, color)
        expected = {
            'room_id': '1234',
            'message': 'locmem test',
            'from': 'TestFrom',
            'format': 'json',
            'message_format': 'html',
            'notify': 0,
            'color': 'yellow'
        }
        self.assertEqual([expected], djhipchat.sent_messages)

    @override_settings(HIPCHAT_BACKEND=_backend('locmem'))
    def test_default_sender(self):
        djhipchat.sent_messages = []
        with override_settings(HIPCHAT_DEFAULT_SENDER='TestSender'):
            djhipchat.send_message('1234', 'test sender')
            self.assertEqual('TestSender', djhipchat.sent_messages[0]['from'])

        djhipchat.sent_messages = []
        with override_settings(HIPCHAT_DEFAULT_SENDER=None):
            djhipchat.send_message('1234', 'test sender')
            self.assertEqual('Django', djhipchat.sent_messages[0]['from'])


@skipUnless(send_message_task, "requires celery")
@override_settings(HIPCHAT_BACKEND=_backend('celery'),
                   HIPCHAT_CELERY_BACKEND=_backend('locmem'))
class CeleryTest(TestCase):
    def test_backend(self):
        backend = get_backend(_backend('celery'))
        self.assertIsNotNone(backend)

        djhipchat.sent_messages = []
        djhipchat.send_message('1234', 'dummy', sender='TestFrom')
        expected = {
            'room_id': '1234',
            'message': 'dummy',
            'from': 'TestFrom',
            'format': 'json',
            'message_format': 'html',
            'notify': 0,
            'color': 'yellow'
        }
        self.assertEqual([expected], djhipchat.sent_messages)
