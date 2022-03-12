from db.sqlalchemy.sqlalchemy import DB
from sqlalchemy import BigInteger, Boolean, Column, DateTime, String
from sqlalchemy.sql import expression
from utils.function_database import UTCNow

from .crud_model import CRUDModel


class ContactMessage(DB.Model, CRUDModel):
    __tablename__ = 'contact_message'

    id = Column(BigInteger, primary_key=True)

    creation_date = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=UTCNow()
    )

    is_reviewed = Column(Boolean, nullable=False, default=expression.false())

    name = Column(String(length=128), nullable=False)

    email = Column(String(length=128), nullable=False)

    message = Column(String(length=1024), nullable=False)
