from flask_jwt_extended import JWTManager
from logic.redis import create_redis_revoke_jwt_token

JWT = JWTManager()


@JWT.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    redis = create_redis_revoke_jwt_token()
    token_in_redis = redis.get(jti)
    return token_in_redis is not None
