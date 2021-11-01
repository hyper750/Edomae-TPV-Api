from adapter.db import DB
from sqlalchemy import BigInteger, Column, Float, ForeignKey, Integer, String

from .crud_model import CRUDModel


# TODO: Implement resource
class CommandMeal(DB.Model, CRUDModel):
    __tablename__ = 'command_meal'

    id = Column(BigInteger, primary_key=True)

    # Command reference
    command = Column(
        BigInteger,
        ForeignKey('command.id', ondelete='CASCADE'),
        nullable=False
    )

    # Meal reference
    meal = Column(
        BigInteger,
        ForeignKey('meal.id', ondelete='CASCADE'),
        nullable=False
    )

    # Number of meals to get
    number = Column(
        Integer,
        nullable=False
    )

    # Extra field, for example 'kebab sin cebolla' hahaha
    extra = Column(String(length=256), nullable=True)

    # Discount of a single command meal
    discount = Column(
        Float(precision=2),
        nullable=True
    )
