# social_media_api/settings.py
from pathlib import Path
import os
<<<<<<< HEAD:social_media_api/social_media_api/settings/base.py
=======
from dotenv import load_dotenv
import dj_database_url

# Load environment variables
load_dotenv()
>>>>>>> 6eff1d2035ce5245b9d1e1d3eb3cd972fe880a31:social_media_api/social_media_api/settings.py

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD:social_media_api/social_media_api/settings/base.py
# SECURITY WARNING: keep the secret key used in development secret!
SECRET_KEY = 'django-insecure-17lfgy0(^$jfun(%feqt6bj0+#xr+*o+sermcva!ag6b98^p@c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow only local development hosts
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# -----------------------
# CSRF Trusted Origins (for API clients like Postman, frontend on localhost:3000)
# -----------------------
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://localhost:3000',  # If you use React/Vue
    'http://127.0.0.1:3000',
]
=======
# Production flag
PRODUCTION = os.getenv('DJANGO_PRODUCTION', 'False').lower() == 'true'

# Security
DEBUG = not PRODUCTION
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-17lfgy0(^$jfun(%feqt6bj0+#xr+*o+sermcva!ag6b98^p@c')
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",") if PRODUCTION else []
>>>>>>> 6eff1d2035ce5245b9d1e1d3eb3cd972fe880a31:social_media_api/social_media_api/settings.py

# Application definition
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'drf_yasg',  # Swagger for API documentation

    # Local apps
    'accounts',
    'posts',
    'notifications',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_media_api.urls'
WSGI_APPLICATION = 'social_media_api.wsgi.application'

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

# Database
<<<<<<< HEAD:social_media_api/social_media_api/settings/base.py
# Use PostgreSQL (make sure it's running locally)
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'socialapi_db',
        'USER': 'socialuser',
        'PASSWORD': 'Elmoun10go@',
        'HOST': 'localhost',
        'PORT': '5432',
=======
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'socialapi_db'),
        'USER': os.getenv('DB_USER', 'socialuser'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'Elmoun10go@'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'OPTIONS': {'connect_timeout': 5},
>>>>>>> 6eff1d2035ce5245b9d1e1d3eb3cd972fe880a31:social_media_api/social_media_api/settings.py
    }
}

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASES["default"] = dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=PRODUCTION)

# Password validation
AUTH_PASSWORD_VALIDATORS = [
<<<<<<< HEAD:social_media_api/social_media_api/settings/base.py
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
=======
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
>>>>>>> 6eff1d2035ce5245b9d1e1d3eb3cd972fe880a31:social_media_api/social_media_api/settings.py
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and Media
STATIC_URL = '/static/'
<<<<<<< HEAD:social_media_api/social_media_api/settings/base.py
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Used when collectstatic is run

# Media files (user-uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.authentication.SessionAuthentication',
    ],
=======
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
>>>>>>> 6eff1d2035ce5245b9d1e1d3eb3cd972fe880a31:social_media_api/social_media_api/settings.py
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
<<<<<<< HEAD:social_media_api/social_media_api/settings/base.py
    # Remove JSONRenderer restriction — allow browsable API
    # Comment out DEFAULT_RENDERER_CLASSES to allow browsable API in dev
    # 'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
=======
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
>>>>>>> 6eff1d2035ce5245b9d1e1d3eb3cd972fe880a31:social_media_api/social_media_api/settings.py
}

# Custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

<<<<<<< HEAD:social_media_api/social_media_api/settings/base.py
# Security Settings (DISABLED for local dev)
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
X_FRAME_OPTIONS = 'SAMEORIGIN'  # Allows admin to work in iframes (e.g., debug toolbar)

# Logging (optional, for dev)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======
# Security headers (production)
if PRODUCTION:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

# Logging
if PRODUCTION:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {'console': {'class': 'logging.StreamHandler'}},
        'root': {'handlers': ['console'], 'level': 'INFO'},
    }
else:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {'level': 'ERROR', 'class': 'logging.FileHandler', 'filename': BASE_DIR / 'logs/django.log'}
        },
        'loggers': {'django': {'handlers': ['file'], 'level': 'ERROR', 'propagate': True}},
    }

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
>>>>>>> 6eff1d2035ce5245b9d1e1d3eb3cd972fe880a31:social_media_api/social_media_api/settings.py
