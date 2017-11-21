# -*- coding: utf-8 -*-
from django.core.exceptions import ImproperlyConfigured
#for django-cms
from django.utils.translation import ugettext_lazy as _
import json

from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

with open("secrets.json") as f:
    secrets = json.loads(f.read())

def get_secret(secret_name, secrets=secrets):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)

SECRET_KEY = get_secret('SECRET_KEY')

DJANGO_APPS = (
    #for django cms
    'djangocms_admin_style',
    #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    #for django-cms
    'django.contrib.sites',
)

LOCAL_APPS = (
    'applications.miscelanea',
    'applications.destinos',
    'applications.experiencias',
    'applications.home',
    'applications.paquetes',
)

THIRD_PARTY_APPS = (
    'ckeditor',
    'sorl.thumbnail',
    'ckeditor_uploader',
    'colorfield',
    #django-cms-apps
    'sekizai',
    'cms',
    'menus',
    'treebeard',
    'filer',
    'easy_thumbnails',
    'mptt',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_column',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# django-cms settings
SITE_ID = 1
CMS_TEMPLATES = [
    ('home.html', 'Home page template'),
    ('cms_templates/home_template.html', 'Plantila home'),
]

#
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #for django-cms
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'ngorgeous.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #for django-cms
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'ngorgeous.wsgi.application'

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/


LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#LANGUAGES for django-cms
LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
    ('pt', _('Portuguese')),
    ('fr', _('French')),
    ('de', _('German')),
)
