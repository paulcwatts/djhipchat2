from __future__ import absolute_import, unicode_literals

from optparse import make_option

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<room_id> <message>'
    help = 'Sends a message to a HipChat room.'
    option_list = BaseCommand.option_list + (
        make_option(
            '-f', '--from',
            action='store',
            dest='sender',
            help='The sender of the message'),
        make_option(
            '--format',
            action='store',
            default='html',
            dest='message_format',
            choices=('text', 'html'),
            help='The format of the message, text or html (default html)'),
        make_option(
            '-n', '--notify',
            action='store_true',
            default=False,
            dest='notify',
            help='Causes a notification to appear in the room'),
        make_option(
            '-c', '--color',
            action='store',
            default='yellow',
            dest='color',
            choices=("yellow", "red", "green", "purple", "gray", "random"),
            help='Color to use for the notification.')
    )
    help = 'Sends a message to a HipChat room.'

    def handle(self, *args, **options):
        if len(args) != 2:
            raise CommandError('Incorrect number of arguments: hipchat ' +
                               self.args)

        kwargs = {
            'sender': options['sender'],
            'message_format': options['message_format'],
            'notify': options['notify'],
            'color': options['color']
        }

        from djhipchat import send_message
        result = send_message(*args, **kwargs)

        if 'error' in result:
            raise CommandError(result['error']['message'])
