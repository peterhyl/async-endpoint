info_dict_config = {
    'version': 1,
    'formatters': {
        'default': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'info.log',
            'backupCount': 3
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['file']
        }
    },
    'disable_existing_loggers': False
}

debug_dict_config = {
    'version': 1,
    'formatters': {
        'default': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'debug.log',
            'backupCount': 3
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    },
    'disable_existing_loggers': False
}
