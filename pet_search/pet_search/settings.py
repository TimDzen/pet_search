import os.path
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-5c4=j(3lqf155ro8ry@fixv)w!)gvkmb!si@^065&^^kj4&ure'


DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pet.apps.PetConfig',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.mailru',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.yandex',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'pet_search.urls'

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

WSGI_APPLICATION = 'pet_search.wsgi.application'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'EMAIL_AUTHENTICATION': True,
        'APP': {
            'client_id': '765721912572-474r229pnvpanjflommpchr02h65lqr7.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
    'odnoklassniki': {
        'EMAIL_AUTHENTICATION': True,
        'APP': {
            'client_id': '512001978095',
            'secret': 'D767643DB08DA16189060CC6',
            'key': 'CQOPCDLGDIHBABABA'
        }
    },
    'vk': {
        'EMAIL_AUTHENTICATION': True,
        'APP': {
            'client_id': '51871196',
            'secret': 'PTFJipPLIxU4W06X3aZI',
            'key': '9f13a2499f13a2499f13a249be9c04df9599f139f13a249fafb2b4f2869aa679dc04b61'
        }
    }
}

SOCIALACCOUNT_FORMS = {
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
    'signup': 'allauth.socialaccount.forms.SignupForm',
}


ACCOUNT_FORMS = {'login': 'pet.forms.MyCustomLoginForm'}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LOGIN_REDIRECT_URL = '/'

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
 
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
