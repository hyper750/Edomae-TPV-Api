from adapter.db import DB, MA
from serialization import FileSerialization
from settings import MEAL_CATEGORY_IMATGES_DIR, MEAL_CATEGORY_URL
from sqlalchemy import BigInteger, Boolean, Column, Integer, String
from sqlalchemy.sql import expression
from utils.file_field import save_file_field

from .crud_model import CRUDModel


class MealCategory(DB.Model, CRUDModel):
    __tablename__ = 'meal_category'

    id = Column(BigInteger, primary_key=True)

    # If the meal category is enabled or not
    enabled = Column(Boolean, nullable=False, default=expression.true())

    # Meal category name, Eg: Entrantes, Postre, Bebida
    name = Column(String(250), unique=True, nullable=False)

    # Category imatge
    imatge = Column(String(250), nullable=False)

    # Order to show on the display, Eg:
    # 1. Entrantes
    # 2. Sushi
    # 3. Platos calientes
    # 4. Postres
    order = Column(Integer, nullable=False)

    def save(self):
        # Save file to static folder
        self.imatge = save_file_field(self.imatge, MEAL_CATEGORY_IMATGES_DIR)
        # Save instance
        return super().save()


class MealCategorySchema(MA.Schema):
    imatge = FileSerialization(
        upload_url=MEAL_CATEGORY_URL,
        attribute='imatge'
    )

    class Meta:
        fields = (
            'id',
            'enabled',
            'name',
            'imatge',
            'order'
        )
