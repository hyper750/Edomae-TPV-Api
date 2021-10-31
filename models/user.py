from adapter.db import DB, MA
from sqlalchemy import BigInteger, Boolean, Column, String
from sqlalchemy.sql import expression

# TODO: Add resource to be able to modify your user and if is admin the other users
# TODO: Be able to add users only for admins
class User(DB.Model):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)

    # Enabled
    enabled = Column(
        Boolean,
        nullable=False,
        server_default=expression.false()
    )

    # Username, eg: hyper75
    username = Column(String(length=320), unique=True, nullable=False)

    # Email, eg: raulmarquespalmer150@gmail.com
    email = Column(String(320), unique=True, nullable=False)

    # Password sha512 hash
    password = Column(String(length=128), nullable=False)

    # Is administrator
    admin = Column(Boolean, nullable=False, server_default=expression.false())
