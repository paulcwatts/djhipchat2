from __future__ import absolute_import, unicode_literals

import djhipchat
from djhipchat.backends.base import HipChatBackendBase


class HipChatBackend(HipChatBackendBase):
    def __init__(self, *args, **kwargs):
        super(HipChatBackend, self).__init__(*args, **kwargs)
        if not hasattr(djhipchat, 'sent_messages'):
            djhipchat.sent_messages = []

    def send_message(self, room_id, message, sender,
                     message_format='html', notify=False, color='yellow'):
        data = self.get_payload(room_id, message, sender,
                                message_format, notify, color)

        djhipchat.sent_messages.append(data)
