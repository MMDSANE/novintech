import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-sn1ocxcfw3@@u4d&k7pu=_bd4u4r_32oh*ehzyf1ts%rupsiqu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['novintech.chbk.app', '127.0.0.1']

# CSRF trusted origins - اضافه کردن دامنه‌ها و آی‌پی‌های مجاز
CSRF_TRUSTED_ORIGINS = [
    'https://novintech.chbk.app',
    'http://novintech.chbk.app',
    'http://127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # our apps
    "landing.apps.LandingConfig",
    "about_us.apps.AboutUsConfig",
    "about_me.apps.AboutMeConfig",
    "cooperation.apps.CooperationConfig",
    "contact_us.apps.ContactUsConfig",  # اضافه کردن contact_us
    "portfolio1.apps.Portfolio1Config",
    "portfolio2.apps.Portfolio2Config",
    "portfolio3.apps.Portfolio3Config",
    "portfolio4.apps.Portfolio4Config",
    "competitions.apps.CompetitionsConfig",
    "question.apps.QuestionConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "core.wsgi.application"

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'novintech455_carl',
        'USER': 'novintech455_carl',
        'PASSWORD': 'JnqUjItT4o17',
        'HOST': 'services.irn9.chabokan.net',
        'PORT': '16584',
    }
}

# Password validation
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
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, images)

# تنظیمات دایرکتوری رسانه‌ها (media files)
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

# تنظیم دایرکتوری استاتیک‌ها
STATICFILES_DIRS = [BASE_DIR / 'static']

# تنظیمات دایرکتوری استاتیک در زمان تولید
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# تنظیم صفحه خطای 404
handler404 = 'landing.views.c404'
