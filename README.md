# HipChat integration for Django

The most complete and configurable HipChat library for Django.

* Configurable backend support, including local memory for testing
* Logging integration
* Out-of-the-box integration with celery for asynchronous sending
* Testing

## Installation

1. Install:
```
pip install djhipchat2
```
2. Add `djhipchat2` to your `INSTALLED_APPS`.
3. Configure your backend, or leave it as the default.

## Usage

The easiest usage is to use `djhipchat.send_message`. The parameters are:


## Configuration

### HIPCHAT_BACKEND

### HIPCHAT_API_TOKEN

### HIPCHAT_DEFAULT_SENDER

## Backends

### djhipchat.backends.celery.HipChatBackend

### djhipchat.backends.dummy.HipChatBackend

### djhipchat.backends.locmem.HipChatBackend

### djhipchat.backends.request.HipChatBackend

