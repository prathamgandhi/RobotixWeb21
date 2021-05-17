"""
Django settings for RobotixWeb project.
Generated by 'django-admin startproject' using Django 3.1.7.
"""

from pathlib import Path
import os
import sys
from decouple import config
from datetime import timedelta
import dj_database_url
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = bool(int(os.environ.get('DEBUG',0)))

DEBUG = os.environ.get('DEBUG', default=False)


heroku_config = os.environ.get('heroku_config', default=False)


ALLOWED_HOSTS = ['.herokuapp.com']
ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS')
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(','))
else:
    ALLOWED_HOSTS = ['localhost','*', '.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #pips
    'corsheaders',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'import_export',
    'django_celery_beat',
    'django_celery_results',
    'phone_field',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',


    #apps
    'users',
    "about",
    'achievements',
    'certificate',
    'contact',
    'events',
    'extras',
    'gallery',
    # 'roboexpo',
    # 'roboPortal',
    # 'workshops',
    'recruitment',
    
]
## FOR Heroku
if heroku_config: 
    INSTALLED_APPS.append('whitenoise.runserver_nostatic')



MIDDLEWARE = [
    #cors
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if heroku_config:
    temp = ['whitenoise.middleware.WhiteNoiseMiddleware']
    for i in range(len(MIDDLEWARE)):
        temp.append(MIDDLEWARE[i])
    MIDDLEWARE = temp

ROOT_URLCONF = 'RobotixWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'RobotixWeb.wsgi.application'


if DEBUG:
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:3000',
        'http://192.168.43.159:3000',
    )
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# if DEBUG:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{}'.format(os.environ.get('POSTGRES_DB')),
        'USER': '{}'.format(os.environ.get('POSTGRES_USER')),
        'PASSWORD' :'{}'.format(os.environ.get('POSTGRES_PASSWORD')),
        'HOST' : '{}'.format(os.environ.get('POSTGRES_HOST')),
        'PORT' : '{}'.format(os.environ.get('POSTGRES_PORT'))
    }

}

db_from_env = dj_database_url.config(conn_max_age=500)
if heroku_config:
    DATABASES['default'].update(db_from_env)
    WHITENOISE_USE_FINDERS = True
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'






# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if heroku_config:
    STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'staticfiles'))
    # MEDIA_ROOT = 'mediafiles'
else:
    STATIC_ROOT = '/vol/web/static'
    MEDIA_ROOT = '/vol/web/media'

#drf

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

}

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'


#auth

AUTH_USER_MODEL = 'users.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SITE_ID=1


#email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.environ.get('EMAIL_HOST', default='localhost')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', default=False)
EMAIL_PORT = os.environ.get('EMAIL_PORT', default=25)

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', default='wandavision5432@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', default='')

#messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
LOGOUT_REDIRECT_URL = '/'

#celery
CELERY_RESULT_BACKEND = "django-db"
BROKER_URL = os.environ.setdefault('REDIS_URL', 'redis://redis:6379/')
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = os.environ.setdefault('REDIS_URL', 'redis://redis:6379/')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

#simple_jwt
SIMPLE_JWT={
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=20),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
}

#swagger
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

django_heroku.settings(locals())