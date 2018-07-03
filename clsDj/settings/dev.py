from clsDj.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cls_development',
        'USER': 'osboxes',
        'PASSWORD': '123passwd',
        'HOST': '',
        'PORT': '5432',
    }
}




