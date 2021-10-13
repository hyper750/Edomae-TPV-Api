from settings import DB, MA
from sqlalchemy import BigInteger, Column, String


class User(DB.Model):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)

    # Username, eg: hyper75
    username = Column(String(length=320), unique=True, nullable=False)

    # Email, eg: raulmarquespalmer150@gmail.com
    email = Column(String(320), unique=True, nullable=False)

    # Password sha512 hash
    password = Column(String(length=128), nullable=False)


class UserSchema(MA.Schema):
    class Meta:
        # Fields to serialize
        fields = (
            'id',
            'username',
            'email'
        )
