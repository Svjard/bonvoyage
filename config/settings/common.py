# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
APPS_ROOT = os.path.join(BASE_DIR, 'src')
sys.path.insert(0, APPS_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'compressor',
  'rest_framework',
  'corsheaders',
  'argonauts',
  'main',
  'authentication',
  'posts'
)

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'static'

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'compressor.finders.CompressorFinder',
)

#MEDIA FILE (user uploaded files)
MEDIA_ROOT = 'mediafiles'

MEDIA_URL = '/mediafiles/'

REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticatedOrReadOnly',
  ),
  'DEFAULT_AUTHENTICATION_CLASSES': (
      'rest_framework.authentication.SessionAuthentication',
      'rest_framework.authentication.BasicAuthentication',
  ),
  'DEFAULT_RENDERER_CLASSES': (
    'utils.api.renderers.CamelCaseJSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
  ),
  'DEFAULT_PARSER_CLASSES': (
    'utils.api.parsers.CamelCaseJSONRenderer',
    'rest_framework.parsers.FormParser',
    'rest_framework.parsers.MultiPartParser'
  ),
  'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
  'PAGE_SIZE': 10
}

# Honor the 'X-Forwarded-Proto' navbar for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
# ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'authentication.Account'

#LOG
LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'handlers': {
    'file': {
      'level': 'DEBUG',
      'class': 'logging.FileHandler',
      'filename': './debug.log',
    }
  },
  'loggers': {
    'django.request': {
      'handlers': ['file'],
      'level': 'DEBUG',
      'propagate': True,
    }
  }
}

#For python-social-auth
# SOCIAL_AUTH_URL_NAMESPACE = 'social'

# SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['email', 'username']

# AUTHENTICATION_BACKENDS = (
#     'social.backends.facebook.FacebookOAuth2',
#     'social.backends.google.GoogleOAuth2',
#     # 'social.backends.twitter.TwitterOAuth',
#     'django.contrib.auth.backends.ModelBackend',
# )