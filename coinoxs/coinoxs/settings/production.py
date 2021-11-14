from .base import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']
# TODO: Make this: os.environ['ALLOWED_HOSTS']
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wagtail',
        'USER': os.environ['POSTGRES_USERNAME'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': '5432',
    }
}

try:
    from .local import *
except ImportError:
    pass
