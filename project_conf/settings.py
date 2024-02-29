import os
from pathlib import Path
from dotenv import load_dotenv
from .django_admin_settings import DJANGO_ADMIN_JAZZMIN_SETTINGS, UI_TWEAKS

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
debug_str = os.getenv("DEBUG")
if debug_str.lower() in ['true', 'yes', '1']:
    DEBUG = True
else:
    DEBUG = False
    
ALLOWED_HOSTS = list(os.getenv('DJANGO_ALLOWED_HOSTS'))


# Application definition
JAZZMIN_APP = [
    'jazzmin',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ]

THIRD_PARTY_APPS = [
    'rangefilter',
]

# Custom apps
PROJECT_APPS = [
    'apps.mainapp',
]

INSTALLED_APPS = JAZZMIN_APP + DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'project_conf.urls'

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

WSGI_APPLICATION = 'project_conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
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
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static/",
]
# STATIC_ROOT = 'static/'
# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
JAZZMIN_SETTINGS = DJANGO_ADMIN_JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS = UI_TWEAKS