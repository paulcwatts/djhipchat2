# HipChat integration for Django

The most complete and configurable HipChat library for Django.

* Configurable backend support, including local memory for testing
* Logging integration
* Out-of-the-box integration with [celery](http://www.celeryproject.org/) for asynchronous sending
* Testing

## Installation

1. Install: `pip install djhipchat2`
2. Add `djhipchat2` to your `INSTALLED_APPS`.
3. Configure your backend, or leave it as the default.

## Usage

### djhipchat.send_message

This will send a HipChat message using the default backend. The parameters are:

### djhipchat.get_backend

Get a reference to a HipChat backend. Each backend has one defined method: `send_message` which has the same parameters as `djhipchat.send_message`.

## Logger

Integrate HipChat into your server logging: this defines a logging handler that sends the message to a HipChat room. You can configure a logger to notify members of the room, or also configure multiple colors for log levels using the same handler. Here is a sample:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'djhipchat': {
            'level': 'INFO',
            'class': 'djhipchat.logger.HipChatHandler',
            'token': '{{your_token_here}}',
            'room' : '{{your_room_id_here}}',
            'sender': 'Myapp',
            'notify': True,
            'color':'green',
            'colors': {
               'ERROR':'red',
               'CRITICAL':'red',
               'WARNING':'yellow',
           }
        }
    },
    'loggers': {
        'test_handler': {
            'handlers': ['djhipchat'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
```

This is inspired by: https://gist.github.com/hugorodgerbrown/3176710

## Configuration

### HIPCHAT_BACKEND

Specifies the default backend to use. The default is `djhipchat.backends.locmem.HipChatBackend`

### HIPCHAT_API_TOKEN

Specifies the HipChat API token. This is theoretically optional except for the request backend, but that's probably what you want to use in production anyway.

### HIPCHAT_DEFAULT_SENDER

The default sender if not specified in a send_message call. If not specified, the default is "Django".

### HIPCHAT_CELERY_BACKEND

When using the Celery backend, it needs a "synchronous" backend to actually send the message. There is no default, so you must specify this in order to use the Celery backend.

## Backends

### djhipchat.backends.celery.HipChatBackend

This backend sends all messages through a [Celery](http://www.celeryproject.org/) task. In order to use this backend, you must have celery installed and specify a synchronous backend in the `HIPCHAT_CELERY_BACKEND` setting.

### djhipchat.backends.dummy.HipChatBackend

Just what is sounds like: this backend does nothing.

### djhipchat.backends.locmem.HipChatBackend

Similar to the locmem email backend in Django, this collects all messages into an array at `djhipchat.sent_messages`. You can use this for testing.

### djhipchat.backends.request.HipChatBackend

This is the default backend, which actually sends your message to HipChat.