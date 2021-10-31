from adapter.db import DB
from settings import MEAL_IMATGES_DIR
from sqlalchemy import (
    BigInteger, Boolean, Column, Float, ForeignKey,
    Integer, String
)
from sqlalchemy.sql import expression
from utils.file_field import save_file_field

from .crud_model import CRUDModel


class Meal(DB.Model, CRUDModel):
    __tablename__ = 'meal'

    id = Column(BigInteger, primary_key=True)

    # Meal enabled or not
    enabled = Column(Boolean, nullable=False, default=expression.true())

    # Meal name
    name = Column(String(length=124), nullable=False, unique=True)

    # Description of the meal, for example the ingredients
    description = Column(String(length=2048), nullable=True)

    # Price in €
    price = Column(Float(precision=2), nullable=False)

    # Category of the meal, Eg: Entrante, Postre...
    category = Column(
        BigInteger,
        ForeignKey('meal_category.id', ondelete='SET NULL'),
        nullable=True
    )

    # Meal imatge path
    imatge = Column(String(250), nullable=False)

    # Order to show on the display
    order = Column(Integer, nullable=False)

    def save(self):
        # Save imatge to dir
        self.imatge = save_file_field(self.imatge, MEAL_IMATGES_DIR)
        # Save instance
        return super().save()
