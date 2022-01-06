from adapter.db import DB
from sqlalchemy import (
    BigInteger, Boolean, Column, Float, ForeignKey,
    Integer, UniqueConstraint
)
from sqlalchemy.sql import expression

from .crud_model import CRUDModel


class Table(DB.Model, CRUDModel):
    __tablename__ = 'table'

    # Id of the table
    id = Column(BigInteger, primary_key=True)

    # Enable or disable table
    enabled = Column(Boolean, nullable=False, default=expression.true())

    # Local reference
    local = Column(
        BigInteger,
        ForeignKey('local.id', ondelete='SET NULL'),
        nullable=True
    )

    # X coordinates to place it inside the local imatge
    x_coordinates = Column(
        Float(precision=2), nullable=False
    )

    # Y coordinates to place it inside the local imatge
    y_coordinates = Column(
        Float(precision=2), nullable=False
    )

    # Table number
    number = Column(Integer, nullable=False)

    # Number of persons
    number_of_persons = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            'local', 'number',
            name='unique_local_and_table_number'
        ),
    )
