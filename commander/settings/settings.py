import os

FLASK_CONFIG = {
    # Production mode
    'DEBUG': False,

    # Secret key
    'SECRET_KEY': os.environ.get('SECRET_KEY'),

    # Database url
    # Eg: postgresql://root:password@127.0.0.1:5432/dbname
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URI'),

    # Disable before and after commit signals
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}
