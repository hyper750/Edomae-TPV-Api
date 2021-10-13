import hashlib

import models
from settings import HASH_NAME, ITERATIONS, SECRET_KEY


def authenticate_user(username: str, password: str) -> models.User:
    hashed_password = hashlib.pbkdf2_hmac(
        HASH_NAME,
        password.encode('utf-8'),
        SECRET_KEY.encode('utf-8'),
        ITERATIONS
    ).hex()
    user = models.User.query.filter_by(
        username=username, password=hashed_password
    ).first()
    return user


def identity_user(payload: dict) -> models.User:
    user_id = payload.get('identity')
    user = models.User.query.filter_by(id=user_id).first()
    return user
