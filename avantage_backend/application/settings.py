import os
from email.policy import default

import environ
from django.db.models import BigAutoField, FileField as DbFileField
from django.forms import FileField as FormFileField, ChoiceField
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
    "https://ooomlk.ru",
    "https://www.ooomlk.ru",
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
        "NAME": env.str("DATABASE_NAME", default="admin"),
        "USER": env.str("DATABASE_USER", default="admin"),
        "PASSWORD": env.str("DATABASE_PASSWORD", default="admin"),
        "HOST": env.str("DATABASE_HOST", default="admin"),
        "PORT": env.int("DATABASE_PORT", default="3306"),
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

STATIC_URL = 'static/'

STATIC_ROOT = '/home/r/raigoreg/raigoreg.beget.tech/public_html/static'

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# if not DEBUG:
# if env.bool("LOGGING_PATH", default=False):
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "LEVEL:%(levelname)s "
            "TIME:%(asctime)s MESSAGE:%(message)s"
        },
    },
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": env.str("LOGGING_PATH"),
            "formatter": "verbose",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        }
    },
}

SERIALIZER_FIELD_MAPPING = {
    BigAutoField: fields.Int,
    DbFileField: fields.Str,
}
SERIALIZER_FORM_FIELD_MAPPING = {
    FormFileField: fields.Str,
    ChoiceField: fields.Str,
}

# EMAIL SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="smtp.mail.ru")
EMAIL_PORT = env("EMAIL_PORT", default=2525)
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=True)
EMAIL_USE_SSL = False
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="admin@mail.com")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="password")
EMAIL_FROM_USER = env("EMAIL_FROM_USER", default="admin@mail.com")

COOPERATION_BID_EMAIL_RECIPIENT = env(
    "EMAIL_FROM_USER", default="admin@mail.com"
)
PRICELIST_BID_EMAIL_RECIPIENT = env("EMAIL_FROM_USER", default="admin@mail.com")
