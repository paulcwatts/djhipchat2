from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module


HIPCHAT_BACKEND = getattr(settings, 'HIPCHAT_BACKEND',
                          'djhipchat.backends.locmem.HipChatBackend')


def get_backend(backend=None, **kwargs):
    path = backend or settings.HIPCHAT_BACKEND
    try:
        mod_name, klass_name = path.rsplit('.', 1)
        mod = import_module(mod_name)
    except ImportError as e:
        raise ImproperlyConfigured(
            ('Error importing HipChat backend module %s: "%s"' %
             (mod_name, e)))
    try:
        klass = getattr(mod, klass_name)
    except AttributeError:
        raise ImproperlyConfigured(('Module "%s" does not define a '
                                    '"%s" class' % (mod_name, klass_name)))
    return klass(**kwargs)


def send_message(room_id, message, sender=None,
                 message_format='html', notify=False,
                 color='yellow'):
    """
    Sends a message to HipChat.

    :param room_id: The ID of the Room to send to.
    :param sender: The text name of the sender.
    :param message: The text or HTML of the message.
    :param message_format: 'text' or 'html'.
    :param notify: Whether to trigger a notification for users in the room.
    :param color: The color of the message.
    """
    sender = (sender or
              getattr(settings, 'HIPCHAT_DEFAULT_SENDER', '') or
              'Django')
    return get_backend().send_message(room_id, message, sender,
                                      message_format, notify, color)
