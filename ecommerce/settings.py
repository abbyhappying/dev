"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#render setup
import environ
env = environ.Env()
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1+tutuw(vxdna1mwfbbxrx=#&qz6l!%s*k25_9rwl01(!3r7m9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['abbystores.com' , 'www.abbystores.com','*'] # * means all of the access

ALLOWED_HOSTS =['*']

# CSRF_TRUSTED_ORIGINS = [''] #decide who is allowed to post in our website


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",#django app
    "cart",#django app
    "account",#django app
    "payment",#django app
    "mathfilters",
    "crispy_forms",
    "storages",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ecommerce.urls"

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
                "store.views.categories",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce.wsgi.application"


# Local django backend sqlite Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS=[BASE_DIR/'static']

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "static/media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#The email host user will send authentication email to the registered user
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

#allow paypal popup in django
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

#AWS accesss key
AWS_ACCESS_KEY_ID = "AKIAR4URLPGA7OIHGGCM"
AWS_SECRET_ACCESS_KEY = "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"

#AWS S3 configuration setting:
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_CUSTOM_DOMAIN ='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_FILE_OVERWRITE = False

#Admin styling adjustment
ADMIN_MEDIA_PREFIX = '/static/admin/'


#AWS RDS database configration setting
# DB_NAME=djangostore
# DB_USER=abbystore
# DB_PASSWORD=abby081285
# DB_HOST=django-project.ctwkzcdojqrg.us-east-2.rds.amazonaws.com
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),  # Host is aws s3 database endpoint
#         'PORT': '5432',  # Use the default PostgreSQL port 5432 if not specified
#     }
# }

#render setup
import dj_database_url

DATABASES = {
    'default':dj_database_url.parse(env('DATABASE_URL'))
}