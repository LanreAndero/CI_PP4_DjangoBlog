import os
from pathlib import Path
from django.contrib.messages import constants as messages
import dj_database_url
if os.path.isfile("env.py"):
    import env  # noqa


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'cy-django-blog-486df1fc929f.herokuapp.com',
    '8000-lanreandero-cipp4django-z0926ut9dsq.ws-eu111.gitpod.io',
    'localhost'
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

ADMIN_URL = 'admin/'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'corsheaders',
    'cloudinary',
    'crispy_forms',
    'crispy_bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_summernote',
    'blog',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

CSRF_COOKIE_SECURE = True

CSRF_COOKIE_SAMESITE = 'None'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'christian_youth_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'christian_youth_blog.wsgi.application'


DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}


CSRF_TRUSTED_ORIGINS = [
    "https://8000-lanreandero-cipp4django-z0926ut9dsq.ws-eu111.gitpod.io",
    "cy-django-blog-486df1fc929f.herokuapp.com"
    "https://*.herokuapp.com",
    "https://*.gitpod.io",
]


CORS_ALLOWED_ORIGINS = [
    "https://8000-lanreandero-cipp4django-z0926ut9dsq.ws-eu111.gitpod.io",
    "cy-django-blog-486df1fc929f.herokuapp.com"
    "https://*.herokuapp.com",
    "https://*.gitpod.io",
    "https://ui.dev",
]

DJANGO_SUMMERNOTE_CONFIG = {
    'iframe': False,
    'summernote': {
        'width': '100%',
        'height': '480',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview']],
        ],
    },
}

ACCOUNT_EMAIL_VERIFICATION = 'none'

SHOULD_APPROVE_USER_POSTS = True


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


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = (
    'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
