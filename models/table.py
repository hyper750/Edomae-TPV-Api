from adapter.db import DB
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, Float

from .crud_model import CRUDModel


class Table(DB.Model, CRUDModel):
    __tablename__ = 'table'

    # Id of the table
    id = Column(BigInteger, primary_key=True)

    # Local reference
    local = Column(
        BigInteger,
        ForeignKey('local.id', ondelete='CASCADE'),
        nullable=False
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
    number = Column(Integer, nullable=False, unique=True)
