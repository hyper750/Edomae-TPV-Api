from db.sqlalchemy.sqlalchemy import DB
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, String
from sqlalchemy.sql import expression
from sqlalchemy.sql.schema import ForeignKey
from utils.function_database import UTCNow

from .crud_model import CRUDModel


class Command(DB.Model, CRUDModel):
    __tablename__ = 'command'

    # Id autoincrement of the command
    id = Column(BigInteger, primary_key=True)

    # User that makes that command
    user = Column(
        BigInteger,
        ForeignKey('user.id', ondelete='SET NULL'),
        nullable=True
    )

    # Command creation date
    creation_date = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=UTCNow()
    )

    # Paid or not
    paid = Column(Boolean, nullable=False, default=expression.false())

    # Paid method
    payment_method = Column(
        BigInteger,
        ForeignKey('payment_method.id', ondelete='SET NULL'),
        nullable=True
    )

    # Discount of the whole meal
    discount = Column(
        Float(precision=2),
        nullable=True
    )

    # Extras
    extra = Column(
        String(length=256),
        nullable=True
    )

    # If the command is a home delivery
    is_home_delivery = Column(
        Boolean,
        default=expression.false(),
        nullable=False,
    )

    # Address of the delivery
    delivery_address = Column(
        String(length=256),
        nullable=True
    )

    # Delivery details
    delivery_details = Column(
        String(length=256),
        nullable=True
    )

    # Assign command table
    table = Column(
        BigInteger,
        ForeignKey('table.id', ondelete='SET NULL'),
        # May be for delivery
        nullable=True
    )

    # Be able to insert a table name, Eg: 'Gul' table
    table_name = Column(
        String(length=256),
        # May be for delivery
        nullable=True
    )
