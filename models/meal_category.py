from adapter.db import DB, MA
from sqlalchemy import BigInteger, Column, String


class MealCategory(DB.Model):
    __tablename__ = 'meal_category'

    id = Column(BigInteger, primary_key=True)

    # Meal category name, Eg: Entrantes, Postre, Bebida
    name = Column(String(250), unique=True, nullable=False)

    # Category imatge
    # TODO: Add custom field that saves the path of the file/imatge and saves the file to folder
    imatge = Column(String(250), nullable=False)


class MealCategorySchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'imatge'
        )