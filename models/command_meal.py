from adapter.db import DB, MA
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String

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
    extra = Column(String, nullable=True)


class CommandMealSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'command',
            'meal',
            'number',
            'extra'
        )
