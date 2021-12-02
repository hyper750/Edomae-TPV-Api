import os
from datetime import timedelta

DEBUG = os.environ.get('DEBUG') in ['True', '1', 't']

HASH_NAME = 'sha512'
SECRET_KEY = os.environ.get('SECRET_KEY')
ITERATIONS = 5000

# JTI token expiration
JTI_EXPIRATION = timedelta(days=1)

FLASK_CONFIG = {
    # Production mode
    'DEBUG': DEBUG,

    # Secret key
    'SECRET_KEY': SECRET_KEY,
    'JWT_SECRET_KEY': SECRET_KEY,

    # Database url
    # Eg: postgresql://root:password@127.0.0.1:5432/dbname
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URI'),

    # Disable before and after commit signals
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,

    # JWT token expiration
    'JWT_ACCESS_TOKEN_EXPIRES': JTI_EXPIRATION,

    # Propagate JWT exceptions to be able to catch through the loader
    'PROPAGATE_EXCEPTIONS': True
}

# Cors settings
CORS_ALLOW_ORIGIN = 'https://[\w\-]+.edomae.es'
if DEBUG:
    CORS_ALLOW_ORIGIN = '*'

CORS_SETTINGS = {
    r'/*': {'origins': CORS_ALLOW_ORIGIN}
}

# Redis settings
REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

# Static files
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

# Root static dir
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = 'static/'

# Meal imatges folder
MEAL_IMATGES_DIR = os.path.join(STATIC_DIR, 'meal')
MEAL_IMATGES_URL = f'{STATIC_URL}meal'

# Meal category imatges folder
MEAL_CATEGORY_IMATGES_DIR = os.path.join(STATIC_DIR, 'mealCategory')
MEAL_CATEGORY_URL = f'{STATIC_URL}mealCategory'
