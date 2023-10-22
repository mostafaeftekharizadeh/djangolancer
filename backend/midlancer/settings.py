"""
midlancer main Settings
"""
import os
from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
env = environ.Env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SITE_ID = 1

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env(
    "SECRET_KEY",
    default="django-insecure-w34chp8@_0iwp2s%g_(=qb!#y3tqqcwtckk-33l^&#f-f8+6+8",  # type: ignore
)

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get("ALLOWED_HOSTS", "").split(","),
    )
)

INSTALLED_APPS = [
    # 'jazzmin',
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "user",
    "location",
    "projects",
    "configuration",
    "complain",
    "money",
    "chat",
    #    'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
    "drf_yasg",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "midlancer.urls"

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

WSGI_APPLICATION = "midlancer.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

if os.environ.get("DB_ENGIN") == "sqlite":
    DATABASES = {
        "default": env.db_url("DB_URL", default="sqlite:///db.sqlite3"),  # type: ignore
    }

if os.environ.get("DB_ENGIN") == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASS"),
            "HOST": os.environ.get("DB_HOST"),
            "PORT": os.environ.get("DB_PORT"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "otp_minute": "16/min",
        "otp_hour": "600/hour",
        "anon": "200/min",
        "user": "400/min",
    },
}

MIDLANCER_APPS = [
    "user",
    "location",
    "projects",
    "configuration",
    "money",
    "complain",
    "chat",
    # 'FileUploader'
]

AUTH_PROFILE_MODULE = "user.Profile"


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1",
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOWED_ORIGINS.extend(
    filter(
        None,
        os.environ.get("CORS_ALLOWED_ORIGINS", "").split(","),
    )
)

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1",
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000/",
]
CSRF_TRUSTED_ORIGINS.extend(
    filter(
        None,
        os.environ.get("CORS_ALLOWED_ORIGINS", "").split(","),
    )
)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "midlancerFormatter": {
            "format": "{name:30s} {asctime} {levelname:7s} {message}",
            "style": "{",
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        },
    },
    "handlers": {
        "midlancerFile": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "log/midlancer-debug.log",
            "formatter": "midlancerFormatter",
        },
    },
    "loggers": {
        "midlancer": {
            "handlers": ["midlancerFile"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

# expire otp code in minutes
OTP_EXPIRE_TIME = 120
# IPPANEL_SECRET = os.environ.get("IPPANEL_SECRET", default="NhFNGQaW7WR4r72tiTGclUrvkpK9VwaKmVMwmdQ1eJ0=")  # type: ignore
IPPANEL_SECRET = "NhFNGQaW7WR4r72tiTGclUrvkpK9VwaKmVMwmdQ1eJ0="  # type: ignore


MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "media/"
STATIC_ROOT = BASE_DIR / "static/"
AUTH_USER_MODEL = "user.User"
LOCALE_PATHS = ["locale"]
LANGUAGES = (
    ("en-us", "English"),
    ("fa-IR", "Persian"),
)
LANGUAGE_CODE = "fa-IR"
AUTHENTICATION_BACKENDS = [
    "library.backends.MidlancerBackend",
    "django.contrib.auth.backends.ModelBackend",
]
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
