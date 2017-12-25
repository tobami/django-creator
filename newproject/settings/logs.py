import os

from .django import INSTALLED_APPS

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
LOG_HANDLERS = ['console']

RAVEN_CONFIG = {'dsn': os.environ.get('RAVEN_DSN')}
if RAVEN_CONFIG['dsn']:
    LOG_HANDLERS.append('sentry')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'newproject': {
            'handlers': LOG_HANDLERS,
            'level': LOG_LEVEL,
            'propagate': False,
        }
    }
}

# Sentry

if RAVEN_CONFIG['dsn']:
    INSTALLED_APPS += [
        'raven.contrib.django.raven_compat',
    ]
    LOGGING['root'] = {
        'level': 'WARNING',
        'handlers': ['sentry'],
    }
    LOGGING['handlers']['sentry'] = {
        'level': 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    }
    LOGGING['loggers']['raven'] = {
        'level': 'DEBUG',
        'handlers': ['console'],
        'propagate': False,
    }
    LOGGING['loggers']['sentry.errors'] = {
        'level': 'DEBUG',
        'handlers': ['console'],
        'propagate': False,
    }
