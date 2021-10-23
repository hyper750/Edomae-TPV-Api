from adapter.db import DB, MA
from flask import request
from marshmallow.fields import Field
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

    def save(self):
        # Save file to static folder
        save_file_field(self.imatge, MEAL_CATEGORY_IMATGES_DIR)
        # Save imatge filename to db
        self.imatge = self.imatge.filename
        # Save instance
        super().save()


class ImatgeSerilization(Field):
    def _serialize(self, value, attr: str, obj, **kwargs):
        if value is None:
            return value

        return f'{request.host_url}{MEAL_CATEGORY_URL}/{value}'


class MealCategorySchema(MA.Schema):
    imatge = ImatgeSerilization(attribute='imatge')

    class Meta:
        fields = (
            'id',
            'name',
            'imatge'
        )
