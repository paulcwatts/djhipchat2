from __future__ import absolute_import, unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from django.test.utils import override_settings

import djhipchat


class BackendTest(TestCase):
    def test_backend_errors(self):
        self.assertRaises(ImproperlyConfigured,
                          lambda: djhipchat.get_backend(
                              'djhipchat.foo.BadModule'))
        self.assertRaises(ImproperlyConfigured,
                          lambda: djhipchat.get_backend(
                              'djhipchat.backends.dummy.BadClass'))

    @override_settings(
        HIPCHAT_BACKEND='djhipchat.backends.dummy.HipChatBackend')
    def test_dummy(self):
        backend = djhipchat.get_backend(
            'djhipchat.backends.dummy.HipChatBackend')
        self.assertIsNotNone(backend)

        djhipchat.sent_messages = []
        djhipchat.send_message('1234', 'dummy')
        self.assertEqual([], djhipchat.sent_messages)

    @override_settings(
        HIPCHAT_BACKEND='djhipchat.backends.locmem.HipChatBackend')
    def test_locmem(self):
        backend = djhipchat.get_backend(
            'djhipchat.backends.locmem.HipChatBackend')
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

    @override_settings(
        HIPCHAT_BACKEND='djhipchat.backends.locmem.HipChatBackend')
    def test_default_sender(self):
        djhipchat.sent_messages = []
        with override_settings(HIPCHAT_DEFAULT_SENDER='TestSender'):
            djhipchat.send_message('1234', 'test sender')
            self.assertEqual('TestSender', djhipchat.sent_messages[0]['from'])

        djhipchat.sent_messages = []
        with override_settings(HIPCHAT_DEFAULT_SENDER=None):
            djhipchat.send_message('1234', 'test sender')
            self.assertEqual('Django', djhipchat.sent_messages[0]['from'])
