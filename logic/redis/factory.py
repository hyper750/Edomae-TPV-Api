from settings import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

from redis import Redis


def create_redis_instance(db: int = 0) -> Redis:
    return Redis(
        REDIS_HOST, REDIS_PORT, db, REDIS_PASSWORD
    )


def create_redis_revoke_jwt_token() -> Redis:
    return create_redis_instance(db=0)
