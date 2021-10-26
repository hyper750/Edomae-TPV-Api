from adapter.db import DB, MA
from sqlalchemy import BigInteger, Boolean, Column, DateTime
from sqlalchemy.sql import expression
from sqlalchemy.sql.schema import ForeignKey
from utils.function_database import UTCNow

from .crud_model import CRUDModel


# TODO: Implement resource
class Command(DB.Model, CRUDModel):
    __tablename__ = 'command'

    # Id autoincrement of the command
    id = Column(BigInteger, primary_key=True)

    # User that makes that command
    user = Column(
        BigInteger,
        ForeignKey('user.id', ondelete='CASCADE'),
        nullable=False
    )

    # Command creation date
    creation_date = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=UTCNow()
    )

    # Command last update
    last_update = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=UTCNow(),
        server_onupdate=UTCNow()
    )

    # Paid or not
    paid = Column(Boolean, nullable=False, default=expression.false())

    # Paid method
    payment_method = Column(
        BigInteger,
        ForeignKey('payment_method.id', ondelete='CASCADE'),
        nullable=True
    )


class CommandSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'user',
            'creation_date',
            'last_update',
            'paid',
            'payment_method'
        )
