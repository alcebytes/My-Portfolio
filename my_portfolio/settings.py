"""
Django settings for my_portfolio project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants
from decouple import config

# ----------------------------------------------------------
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# ----------------------------------------------------------
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# ----------------------------------------------------------
# Allowed Hosts
# --- development --- #
if DEBUG:
	ALLOWED_HOSTS = []

# --- Production --- #
if not DEBUG:
	ALLOWED_HOSTS = [config('ALLOWED_HOSTS')]

# ----------------------------------------------------------
# SSL and Cookies
# ----- Production ----- #
if not DEBUG:
	SECURE_SSL_REDIRECT = True
	SESSION_COOKIE_SECURE = True
	CSRF_COOKIE_SECURE = True

# ----------------------------------------------------------
# Application definition

INSTALLED_APPS = [
	# --- Accounts --- #
	'accounts',

	# --- Django Apps --- #
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	# --- system apps --- #
	'base',
	'principal',
]

# --- Only for use whit Cloudinary media files storage --- #
if not DEBUG:
	INSTALLED_APPS[7:7] = 'cloudinary_storage', 'cloudinary'

# --- Summernote --- #
X_FRAME_OPTIONS = 'SAMEORIGIN'

# ----------------------------------------------------------
MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------------------------------------
ROOT_URLCONF = 'my_portfolio.urls'

# ----------------------------------------------------------
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

# ----------------------------------------------------------
WSGI_APPLICATION = 'my_portfolio.wsgi.application'

# ----------------------------------------------------------
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# --- Sqlite --- #
# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.sqlite3',
# 		'NAME': BASE_DIR / 'db.sqlite3',
# 	}
# }

# --- PostgreSQL Development and production with db data--- #
# DATABASES = {
# 		'default': {
# 			'ENGINE': 'django.db.backends.postgresql',
# 			'NAME': config('NAME_DB'),
# 			'USER': config('USER_DB'),
# 			'PASSWORD': config('PASSWORD_DB'),
# 			'HOST': config('HOST_DB'),
# 			'PORT': config('PORT_DB'),
# 		}
# 	}


# --- PostgreSQL in Heroku--- #
# --- Development --- #
if DEBUG:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql',
			'NAME': config('NAME_DB'),
			'USER': config('USER_DB'),
			'PASSWORD': config('PASSWORD_DB'),
			'HOST': config('HOST_DB'),
			'PORT': config('PORT_DB'),
		}
	}

# --- Prodution --- #
if not DEBUG:
	import dj_database_url

	DATABASES = {
		'default': dj_database_url.config(
			conn_max_age=600,
			ssl_require=True
		)
	}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Lisbon'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ----------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# --- development --- #
if DEBUG:
	STATIC_ROOT = BASE_DIR / 'static'
	MEDIA_ROOT = BASE_DIR / 'media'

# --- Production --- #
if not DEBUG:
	# STATIC_ROOT = config('STATIC_ROOT')
	# MEDIA_ROOT = config('MEDIA_ROOT')

	# --- For Heroku --- #
	STATIC_ROOT = BASE_DIR / 'staticfiles'

	# --- Only for use whit Cloudinary media files storage --- #
	CLOUDINARY_STORAGE = {
		'CLOUD_NAME': config('CLOUD_NAME'),
		'API_KEY': config('API_KEY'),
		'API_SECRET': config('API_SECRET')
	}

	DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# ----------------------------------------------------------
# --- Email --- #

# --- development --- #
if DEBUG:
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# --- Production --- #
if not DEBUG:
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_HOST = config('EMAIL_HOST')
	EMAIL_HOST_USER = config('EMAIL_HOST_USER')
	EMAIL_PORT = config('EMAIL_PORT', cast=int)
	# EMAIL_USER_SSL = True
	EMAIL_USE_TLS = True
	EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
	DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

	ADMINS = [(config('SUPER_USER'), config('EMAIL'))]
	MANAGERS = ADMINS


# ----------------------------------------------------------
# --- Custom User Model --- #
AUTH_USER_MODEL = 'accounts.CustomUser'


# ----------------------------------------------------------
# --- Login Logout User --- #
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'


# ----------------------------------------------------------
# Mensagens
MESSAGE_TAGS = {
	constants.ERROR: 'alert-danger',
	constants.WARNING: 'alert-warning',
	constants.DEBUG: 'alert-info',
	constants.SUCCESS: 'alert-success',
	constants.INFO: 'alert-info',
}


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
