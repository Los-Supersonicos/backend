from mvp.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432')
    }
}

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

DEBUG = False

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')