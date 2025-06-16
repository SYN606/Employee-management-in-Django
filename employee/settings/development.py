from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-^&!qub_*@8)5v0o4=h_$$r(37k0-w^#+4^6fjl@108k_lu5_s+')

# Allow all hosts in development
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS if host.strip()]

# Optional: use SQLite for development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Optional: enable Django Debug Toolbar or dev tools
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
