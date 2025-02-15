"""
Django settings for jathan_backend project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^c)el!_w=o&o-!d)$uua!k#s@ss*$_rqx=a9p5$21&ct(#y3)u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # CORS Headers (ใช้จัดการ CORS สำหรับ API)
    "corsheaders",

    # Django REST Framework (สำหรับสร้าง API)
    "rest_framework",
    "rest_framework.authtoken",  # ใช้ Token Authentication

    # DJ-Rest-Auth (จัดการ Authentication API)
    "dj_rest_auth.registration",  
    "dj_rest_auth", 
    "django_filters", 

    # Allauth (ใช้จัดการระบบบัญชีผู้ใช้)
    "django.contrib.sites", 
    "allauth",
    "allauth.account",  

    # Allauth Social Accounts (รองรับการล็อกอินด้วยโซเชียล เช่น Google)
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google", 

    # Local Apps (แอปที่สร้างขึ้นเองในโปรเจกต์)
    "accounts",  # จัดการบัญชีผู้ใช้
    "boards",  # ระบบบอร์ดหรือกระดานงาน
    "notifications", # ระบบแจ้งเตือน (Notification)
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # cors header middleware
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = 'jathan_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'jathan_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# allauth
SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# rest-framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )
}

# simple jwt
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=15),  
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

# rest auth
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'access',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh',
    'JWT_AUTH_HTTPONLY': True,
    'SESSION_LOGIN': False,
    'OLD_PASSWORD_FIELD_ENABLED': True,
}



CORS_ALLOW_CREDENTIALS = True

# send email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pong34811@gmail.com'
EMAIL_HOST_PASSWORD = 'dbhd jkxr mwgp xvun'

AUTH_USER_MODEL = "accounts.CustomUserModel"


# LINE API Configuration
LINE_CLIENT_ID = '2006912258'
LINE_CLIENT_SECRET = 'ede0f9c3f18b7c371d70d096a6212b04'
LINE_REDIRECT_URI = 'http://localhost:3000/settings'

LINE_BOT_ACCESS_TOKEN = "p+LZXvFOhO3OXsXHhYul1Yjj707zzteP6TXVPBXWiy2Qz1kP3z5udHzn+xS6LX0+sJXd4EOcVKdqdDfqqV3vtz4NMGeMfqZspkzxm0GB52vILXzbtmv1apBjqQvlNYcZDQd7VgtdlsmDHfij3BWdqwdB04t89/1O/w1cDnyilFU="
