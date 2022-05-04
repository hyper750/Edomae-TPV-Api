from db.sqlalchemy.sqlalchemy import DB
from sqlalchemy import BigInteger, Column, Enum, String, UniqueConstraint

from models.crud_model import CRUDModel
from models.language import Language


class Translation(DB.Model, CRUDModel):

    ___tablename__ = 'translation'

    __table_args__ = (
        UniqueConstraint('key', 'language', name='key_language_uc'),
    )

    # Translation id
    id = Column(BigInteger, primary_key=True)

    # Given a key to translate
    key = Column(
        String(length=2048),
        nullable=False
    )

    # And given a language, translate the content to that language
    language = Column(
        Enum(Language),
        nullable=False
    )

    # We have a translation
    value = Column(
        String(length=2048),
        nullable=False
    )
