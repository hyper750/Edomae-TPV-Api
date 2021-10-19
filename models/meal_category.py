from adapter.db import DB, MA
from sqlalchemy import BigInteger, Column, String


class MealCategory(DB.Model):
    __tablename__ = 'meal_category'

    id = Column(BigInteger, primary_key=True)

    name = Column(String(250), unique=True)


class MealCategorySchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'name'
        )
