from .base import *

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standart': {
            'format': '%(asctime)s %(filename)s [%(levelname)s]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standart'
        },
        'api': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'standart',
            'filename': os.path.join(BASE_DIR, 'api.log'),
        },
    },
    'loggers': {
        'app': {
            'level': 'INFO',
            'handlers': ['api', 'console'],
        },
    }
}
