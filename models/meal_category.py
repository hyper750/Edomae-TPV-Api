from adapter.db import DB, MA
from serialization import FileSerialization
from settings import MEAL_CATEGORY_IMATGES_DIR, MEAL_CATEGORY_URL
from sqlalchemy import BigInteger, Column, String
from utils.file_field import save_file_field

from .crud_model import CRUDModel


class MealCategory(DB.Model, CRUDModel):
    __tablename__ = 'meal_category'

    id = Column(BigInteger, primary_key=True)

    # Meal category name, Eg: Entrantes, Postre, Bebida
    name = Column(String(250), unique=True, nullable=False)

    # Category imatge
    imatge = Column(String(250), nullable=False)

    # TODO: Add order to show on the display

    def save(self):
        # Save file to static folder
        save_file_field(self.imatge, MEAL_CATEGORY_IMATGES_DIR)
        # Save imatge filename to db
        self.imatge = self.imatge.filename
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
            'name',
            'imatge'
        )
