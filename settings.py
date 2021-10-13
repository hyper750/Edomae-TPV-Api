import os

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

HASH_NAME = 'sha512'
SECRET_KEY = os.environ.get('SECRET_KEY')
ITERATIONS = 5000


FLASK_CONFIG = {
    # Production mode
    'DEBUG': os.environ.get('DEBUG') in ['True', '1', 't'],

    # Secret key
    'SECRET_KEY': SECRET_KEY,

    # Database url
    # Eg: postgresql://root:password@127.0.0.1:5432/dbname
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URI'),

    # Disable before and after commit signals
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}


DB = SQLAlchemy()
MA = Marshmallow()
