from adapter.db import DB, MA
from sqlalchemy import BigInteger, Boolean, Column, String, Float
from sqlalchemy.sql import expression


class Meal(DB.Model):
    __tablename__ = 'meal'

    id = Column(BigInteger, primary_key=True)

    # Meal enabled or not
    enabled = Column(Boolean, nullable=False, default=expression.true())

    # Meal name
    name = Column(String(length=124), nullable=False, unique=True)

    # Price in €
    price = Column(Float(precision=2), nullable=False)

    # Meal imatge path
    imatge_name = Column(String(250), nullable=False)


class MealSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'enabled',
            'name',
            'price',
            'imatge_name'
        )
