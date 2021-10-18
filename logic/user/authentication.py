import hashlib

import models
from adapter.redis import create_redis_revoke_jwt_token
from flask_jwt_extended import JWTManager
from settings import HASH_NAME, ITERATIONS, JTI_EXPIRATION, SECRET_KEY

JWT = JWTManager()


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
    redis.set(jti, '', ex=JTI_EXPIRATION)


@JWT.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    redis = create_redis_revoke_jwt_token()
    token_in_redis = redis.get(jti)
    return token_in_redis is not None


@JWT.expired_token_loader
def custom_expired_token_response(jwt_header, jwt_payload):
    return {
        'message': 'Access token expired'
    }, 401


@JWT.revoked_token_loader
def custom_revoked_token_response(jwt_header, jwt_payload):
    return {
        'message': 'Access token revoked'
    }, 401
