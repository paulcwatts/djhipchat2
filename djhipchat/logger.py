"""
Custom log handler for posting log messages to HipChat.

The API documentation is available at:
    https://www.hipchat.com/docs/api/method/rooms/message
The room id can be found by going to:
    https://{{your-account}}.hipchat.com/rooms/ids
The tokens can be set at https://{{your-account}}.hipchat.com/admin/api

Inspired by: https://gist.github.com/hugorodgerbrown/3176710
"""
from __future__ import absolute_import, unicode_literals

from logging import Handler

from djhipchat import send_message


class HipChatHandler(Handler):
    """
    Log handler used to send notifications to HipChat
    """
    def __init__(self, room_id, colors=None, **kwargs):
        """
        Arguments match those of send_message, with the exception of:
        :param colors: A dict of level: color pairs used to override
                    the default color.
        """
        super(HipChatHandler, self).__init__()
        self.room_id = room_id
        self.kwargs = kwargs
        self.colors = colors or {}

    def emit(self, record):
        """
        Sends the record info to HipChat
        """
        kwargs = {
            'room_id': self.room_id,
            'message': record.getMessage(),
            'message_format': 'text'
        }
        kwargs.update(self.kwargs)
        if record.levelname in self.colors:
            kwargs['color'] = self.colors[record.levelname]
        send_message(**kwargs)
