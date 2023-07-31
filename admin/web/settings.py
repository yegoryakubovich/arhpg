import os
from pathlib import Path

import pymysql
from environs import Env

from .check_folders import check_folders
from .config import web_settings


BASE_DIR = Path(__file__).resolve().parent.parent
pymysql.install_as_MySQLdb()

SECRET_KEY = 'django-insecure-n+*62!z*a5l$a6&!hooi0@b5$i-n0#i@fbrfcjtuk3!2ebu63r'
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', web_settings.ADMIN_WEB_IP]
# CSRF_TRUSTED_ORIGINS = [f"https://{web_settings.ADMIN_WEB_IP}", f"https://www.{web_settings.ADMIN_WEB_IP}"]

# Application definition
INSTALLED_APPS = [
    'admin_web',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': web_settings.DB_NAME,
        'USER': web_settings.DB_USER,
        'PASSWORD': web_settings.DB_PASSWORD,
        'HOST': web_settings.DB_HOST,
        'PORT': web_settings.DB_PORT,
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static", ]
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
check_folders()

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
