from adapter.db import DB, MA
from sqlalchemy import BigInteger, Boolean, Column, String
from sqlalchemy.sql import expression

from .crud_model import CRUDModel

# TODO: Add resource
class PaymentMethod(DB.Model, CRUDModel):
    __tablename__ = 'payment_method'

    id = Column(BigInteger, primary_key=True)

    # Payment method enabled or not
    enabled = Column(Boolean, nullable=False, default=expression.true())

    # Payment method name, Eg: 'Credit card', 'Efectivo'
    name = Column(
        String(length=124),
        nullable=False,
        unique=True
    )


class PaymentMethodSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'enabled',
            'name'
        )
