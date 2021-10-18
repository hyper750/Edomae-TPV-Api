from adapter.db import DB, MA
from sqlalchemy import BigInteger, Boolean, Column, String
from sqlalchemy.sql import expression


class User(DB.Model):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)

    # Username, eg: hyper75
    username = Column(String(length=320), unique=True, nullable=False)

    # Email, eg: raulmarquespalmer150@gmail.com
    email = Column(String(320), unique=True, nullable=False)

    # Password sha512 hash
    password = Column(String(length=128), nullable=False)

    # Is administrator
    admin = Column(Boolean, nullable=False, server_default=expression.false())


class UserSchema(MA.Schema):
    class Meta:
        # Fields to serialize
        fields = (
            'id',
            'username',
            'email',
            'admin'
        )
