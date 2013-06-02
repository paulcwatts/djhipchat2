from __future__ import absolute_import, unicode_literals

import requests

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from djhipchat.backends.base import HipChatBackendBase


HIPCHAT_API_URL = 'https://api.hipchat.com/v1/rooms/message'


class HipChatBackend(HipChatBackendBase):
    def __init__(self, *args, **kwargs):
        super(HipChatBackend, self).__init__(*args, **kwargs)

    def send_message(self, room_id, message, sender,
                     message_format='html', notify=False, color='yellow'):
        token = getattr(settings, 'HIPCHAT_API_TOKEN', '')
        if not token:
            raise ImproperlyConfigured("HipChat API token not set")

        data = self.get_payload(room_id, message, sender,
                                message_format, notify, color)
        data['auth_token'] = token

        result = requests.post(HIPCHAT_API_URL, data=data)
        if 'error' in result:
            raise ValueError(result['error']['message'])
