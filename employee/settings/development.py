from .base import *
import os

SECRET_KEY = "django-insecure-^&!qub_*@8)5v0o4=h_$$r(37k0-w^#+4^6fjl@108k_lu5_s+'"

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
