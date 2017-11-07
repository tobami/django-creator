import os

from .django import INSTALLED_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    }
}

# Sentry
RAVEN_CONFIG = {'dsn': os.environ.get('RAVEN_DSN')}

if RAVEN_CONFIG['dsn']:
    INSTALLED_APPS += [
        'raven.contrib.django.raven_compat',
    ]
    LOGGING['handlers']['sentry'] = {
        'level': 'WARNING',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    }

LOGGING['loggers'] = {
    'django': {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': False,
    },
    'newproject': {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': False,
    }
}
