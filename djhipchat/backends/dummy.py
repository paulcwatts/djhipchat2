from __future__ import absolute_import, unicode_literals

from djhipchat.backends.base import HipChatBackendBase


class HipChatBackend(HipChatBackendBase):
    """
    Dummy backend. Doesn't do anything.
    """
    def __init__(self, *args, **kwargs):
        super(HipChatBackend, self).__init__(*args, **kwargs)

    def send_message(self, room_id, message, sender,
                     message_format='html', notify=False, color='yellow'):
        pass
