import os

from signals.settings.base import *  # noqa

from .zds import *  # noqa

SECRET_KEY = 'insecure'
DEBUG = True
ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DATAPUNT_AUTHZ['ALWAYS_OK'] = True  # noqa
SITE_DOMAIN = 'localhost:8000'

INSTALLED_APPS += [  # noqa
    'debug_toolbar',
]
MIDDLEWARE.append(  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEST_LOGIN = os.getenv('TEST_LOGIN', 'signals.admin@example.com')

IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = 'imagekit.cachefiles.strategies.Optimistic'

# ML_TOOL_ENDPOINT = 'https://acc.api.data.amsterdam.nl/signals_mltool'

try:
    from signals.settings.local import *  # noqa
except ImportError:
    pass


def show_toolbar(request):
    return False  # True to enable Django Debug Toolbar (very slow)


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

# Search settings
SEARCH = {
    'PAGE_SIZE': 500,
    'CONNECTION': {
        'URL': 'elasticsearch:9200',
        'INDEX': 'sia_signals',
    },
}

FEATURE_FLAGS['API_VALIDATE_EXTRA_PROPERTIES'] = True  # noqa F405
FEATURE_FLAGS['API_SEARCH_ENABLED'] = True  # noqa F405
FEATURE_FLAGS['SEARCH_BUILD_INDEX'] = True  # noqa F405

# Set console logging to DEBUG
LOGGING['handlers'].update({  # noqa F405
    'console': {
        'level': 'WARNING',
        'class': 'logging.StreamHandler',
        'formatter': 'console',
    },
})

# Log queries to the console
LOGGING['loggers'].update({  # noqa F405
    'django.db.backends': {
        'level': 'WARNING',
        'handlers': ['console', ],
    }
})
