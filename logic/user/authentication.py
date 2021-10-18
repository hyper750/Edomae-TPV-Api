import hashlib

import models
from logic.redis import create_redis_revoke_jwt_token
from settings import HASH_NAME, ITERATIONS, JTI_EXPIRATION, SECRET_KEY


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


def revoke_access_token(jti: str):
    redis = create_redis_revoke_jwt_token()
    redis.set(jti, None, ex=JTI_EXPIRATION)
