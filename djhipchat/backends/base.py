from __future__ import unicode_literals


class HipChatBackendBase(object):
    def get_payload(self, room_id, message, sender,
                    message_format='html',
                    notify=False,
                    color='yellow'):
        data = {
            'room_id': room_id,
            'from': sender,
            'message': message,
            'message_format': message_format,
            'notify': 1 if notify else 0,
            'color': color,
            'format': 'json'
        }
        return data
