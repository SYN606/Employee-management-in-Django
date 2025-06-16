from .base import *
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Secret key
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-fallback-secret-key")

# Allowed hosts (comma-separated in .env)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS if host.strip()]

# Optional: production database setup from env
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv("DB_NAME", ""),
#         'USER': os.getenv("DB_USER", ""),
#         'PASSWORD': os.getenv("DB_PASSWORD", ""),
#         'HOST': os.getenv("DB_HOST", "localhost"),
#         'PORT': os.getenv("DB_PORT", "5432"),
#     }
# }

# Static files directory for production
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Optional: Security settings for production
# SECURE_HSTS_SECONDS = 31536000
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
