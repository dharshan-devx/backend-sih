"""
Django settings for credit project.
"""

import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# BASIC SETTINGS
# ============================================================

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-$-+zrwmz0-ymk!2a4eyt!3v+x54lz313g5z_z+gc!^o*277@91"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = ["*"]

# ============================================================
# APPLICATION DEFINITION
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise for production static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'credit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'credit.wsgi.application'

# ============================================================
# DATABASE CONFIGURATION
# ============================================================

if os.environ.get("RENDER"):
    # Running on Render → Use PostgreSQL
    DATABASES = {
        "default": dj_database_url.parse(os.environ["DATABASE_URL"])
    }
elif os.environ.get("RAILWAY"):
    # Running on Railway → Use PostgreSQL
    DATABASES = {
        "default": dj_database_url.parse(os.environ["DATABASE_URL"])
    }
else:
    # Local development → Use SQLite
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ============================================================
# AUTHENTICATION PASSWORD VALIDATORS
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = 'en'
USE_I18N = True

LANGUAGES = [
    ('as', _('Assamese')),
    ('bn', _('Bengali')),
    ('brx', _('Bodo')),
    ('doi', _('Dogri')),
    ('en', _('English')),
    ('gu', _('Gujarati')),
    ('hi', _('Hindi')),
    ('kn', _('Kannada')),
    ('ks', _('Kashmiri')),
    ('kok', _('Konkani')),
    ('mai', _('Maithili')),
    ('ml', _('Malayalam')),
    ('mni', _('Manipuri')),
    ('mr', _('Marathi')),
    ('ne', _('Nepali')),
    ('or', _('Odia')),
    ('pa', _('Punjabi')),
    ('sa', _('Sanskrit')),
    ('sat', _('Santali')),
    ('sd', _('Sindhi')),
    ('ta', _('Tamil')),
    ('te', _('Telugu')),
    ('ur', _('Urdu')),
]

LOCALE_PATHS = [BASE_DIR / 'locale']

TIME_ZONE = 'UTC'
USE_TZ = True

# ============================================================
# STATIC & MEDIA FILES
# ============================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise compressed static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ============================================================
# CORS SETTINGS
# ============================================================

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# ============================================================
# EMAIL CONFIG (Twilio / Gmail SMTP)
# ============================================================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "sanapathisumanth2119@gmail.com")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ============================================================
# TWILIO CONFIG
# ============================================================

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM_PHONE = os.environ.get("TWILIO_FROM_PHONE")

# ============================================================
# DEFAULT PRIMARY KEY FIELD TYPE
# ============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'