from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config('DB_NAME'),
        "USER": config('DB_USER'),
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": config('DB_HOST'),
        "PORT": config('DB_PORT'),
    }
}


EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')

LOG_ROOT = config('LOG_ROOT')

LOGGING = {
    'version': 1.0,
    'handlers': {
        'django_logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/django.log",
            'maxBytes': 50000,
            'backupCount': 2,
        },
        'db_logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/db.log",
            'maxBytes': 50000,
            'backupCount': 2,
        },
        'celery_logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/celery.log",
            'maxBytes': 50000,
            'backupCount': 2,
        },
        'common_logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/common.log",
            'maxBytes': 50000,
            'backupCount': 2,
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'django_logfile'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['console', 'db_logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'celery.task': {
            'handlers': ['console', 'celery_logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['common_logfile'],
            'propagate': True,
            'level': 'DEBUG',
        },

    }
}

CSRF_COOKIE_HTTPONLY = True
