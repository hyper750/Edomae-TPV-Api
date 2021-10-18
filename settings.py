import os
from datetime import timedelta

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

HASH_NAME = 'sha512'
SECRET_KEY = os.environ.get('SECRET_KEY')
ITERATIONS = 5000

# JTI token expiration
JTI_EXPIRATION = timedelta(days=1)

FLASK_CONFIG = {
    # Production mode
    'DEBUG': os.environ.get('DEBUG') in ['True', '1', 't'],

    # Secret key
    'SECRET_KEY': SECRET_KEY,
    'JWT_SECRET_KEY': SECRET_KEY,

    # Database url
    # Eg: postgresql://root:password@127.0.0.1:5432/dbname
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URI'),

    # Disable before and after commit signals
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,

    # JWT token expiration
    'JWT_ACCESS_TOKEN_EXPIRES': JTI_EXPIRATION
}


DB = SQLAlchemy()
MA = Marshmallow()

# Redis settings
REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
