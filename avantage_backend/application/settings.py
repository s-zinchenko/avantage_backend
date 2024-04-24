import os
from email.policy import default
from logging.handlers import SysLogHandler

import environ
from django.db.models import BigAutoField, FileField as DbFileField
from django.forms import FileField as FormFileField, ChoiceField, NullBooleanField
from marshmallow import fields

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

VERSION = "0.0.1"
env = environ.Env()
environ.Env.read_env(env.str("ENV_PATH", "env"))

SECRET_KEY = env.str("SECRET_KEY", default="my-secret-key")
DEBUG = env.bool("DEBUG", default=False)
SILK = env.bool("SILK", default=False)

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "solo",
    # "import_export",
    "corsheaders",
]

PROJECT_APPS = [
    "avantage_backend.bids",
    "avantage_backend.blog",
    "avantage_backend.cooperation",
    "avantage_backend.core",
    "avantage_backend.goods",
    "avantage_backend.wiki",
]

INSTALLED_APPS += PROJECT_APPS

if SILK:
    INSTALLED_APPS += ["silk"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://localhost:3000',
    'http://127.0.0.1:3000',
    'https://127.0.0.1:3000',
]

if SILK:
    MIDDLEWARE = ["silk.middleware.SilkyMiddleware"] + MIDDLEWARE

ROOT_URLCONF = "avantage_backend.application.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "avantage_backend.application.passenger_wsgi.application"

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.mysql",
        "ENGINE": "django.db.backends.sqlite3",
        # "NAME": "/home/r/raigoreg/raigoreg.beget.tech/public_html/avantage_backend/avantage_admin",
        # "NAME": "avantage_admin",
        "NAME": "avantage_admin_prod",
        # "USER": env.str("DATABASE_USER", default="admin"),
        # "PASSWORD": env.str("DATABASE_PASSWORD", default="admin"),
        # "HOST": env.str("DATABASE_HOST", default="admin"),
        # "PORT": env.int("DATABASE_PORT", default="3306"),
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

AUTH_USER_MODEL = "core.User"

LANGUAGE_CODE = "ru-RU"
TIME_ZONE = "Europe/Moscow"


USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = env("MEDIA_ROOT", default=os.path.join(BASE_DIR, "media"))
MEDIA_URL = "/media/"

# STATIC_URL = "/dj_static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = '/static/'

# STATIC_ROOT = '/home/r/raigoreg/raigoreg.beget.tech/public_html/static'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (

)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

if not DEBUG:
# if env.bool("LOGGING_PATH", default=False):
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                # exact format is not important, this is the minimum information
                "format": "%(created)f %(asctime)s.%(msecs)03d [%(process)d] "
                          "[%(name)s::%(module)s:%(funcName)s:%(lineno)d] "
                          "%(levelname)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "class": "logging.Formatter",
            },
        },
        "handlers": {
            "file": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "filename": env.str("LOGGING_PATH", default="./requests_log.txt"),
            },
        },
        "loggers": {
            "": {"level": "INFO", "handlers": ["file"]},
            "django.db.backends": {  # type: ignore
                "level": "DEBUG",
                "propagate": False,
                "handlers": ["file"]
            },
        }
    }


SERIALIZER_FIELD_MAPPING = {
    BigAutoField: fields.Int,
    DbFileField: fields.Str,
}
SERIALIZER_FORM_FIELD_MAPPING = {
    FormFileField: fields.Str,
    ChoiceField: fields.Str,
    NullBooleanField: fields.Boolean,
}

# EMAIL SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 587
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="semeonzin4enko@yandex.ru")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="pjjnrnxcqqtfwquz")
# EMAIL_FROM_USER = env("EMAIL_FROM_USER", default="zinchieko02@mail.com")

EMAIL_SERVER = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

COOPERATION_BID_EMAIL_RECIPIENT = env(
    "EMAIL_FROM_USER", default="admin@mail.com"
)
PRICELIST_BID_EMAIL_RECIPIENT = env("EMAIL_FROM_USER", default="admin@mail.com")
