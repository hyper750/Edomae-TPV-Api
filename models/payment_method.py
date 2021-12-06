from adapter.db import DB
from settings import PAYMENT_METHOD_IMATGES_DIR
from sqlalchemy import BigInteger, Boolean, Column, String
from sqlalchemy.sql import expression
from utils.file_field import save_file_field
from werkzeug.datastructures import FileStorage

from .crud_model import CRUDModel


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

    # Imatge filename path
    image = Column(String(250), nullable=False)

    def save(self):
        if isinstance(self.image, FileStorage):
            self.image = save_file_field(
                self.image, PAYMENT_METHOD_IMATGES_DIR
            )
        return super().save()
