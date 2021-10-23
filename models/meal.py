from adapter.db import DB, MA
from sqlalchemy import BigInteger, Boolean, Column, Float, ForeignKey, String
from sqlalchemy.sql import expression

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
    # TODO: Add custom field that saves the path of the file/imatge and saves the file to folder
    imatge = Column(String(250), nullable=False)


class MealSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'enabled',
            'name',
            'category',
            'description',
            'price',
            'imatge'
        )
