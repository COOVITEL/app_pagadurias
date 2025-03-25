from pathlib import Path
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)=u!@gy-vke_k!0o2uy3x&==f(a$)qkpnd%ktm0gl@6x*!zpll'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'account.User'

AUTH_LDAP_SERVER_URI = os.getenv("URL")

AUTH_LDAP_BIND_DN = os.getenv("USER")
AUTH_LDAP_BIND_PASSWORD = os.getenv("PASSWORD")

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "OU=Users,OU=COOVITEL,DC=coovitel,DC=local",
    ldap.SCOPE_SUBTREE,
    "(sAMAccountName=%(user)s)"
)

# AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
#     "OU=Users,OU=COOVITEL,DC=coovitel,DC=local",
#     ldap.SCOPE_SUBTREE,
#     "(objectClass=group)"
# )

# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

# AUTH_LDAP_REQUIRE_GROUP = 'CN=GRPTI,OU=Grupos,OU=COOVITEL,DC=coovitel,DC=local'

AUTH_LDAP_USER_ATTR_MAP = { 
    "first_name": "givenName", 
    "last_name": "sn", 
    "email": "mail" 
}

AUTHENTICATION_BACKENDS = (
    # 'account.authentication.CustomLDAPBackend',
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tailwind',
    'theme',
    'django_browser_reload',
    'administrador',
    'pagadurias',
    'citas',
    'account',
    'operaciones',
    'estadisticas',
    'widget_tweaks',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    # 'app_pagadurias.middleware.ResgRestrictAccessMiddleware',
]

ROOT_URLCONF = 'app_pagadurias.urls'

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

WSGI_APPLICATION = 'app_pagadurias.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
