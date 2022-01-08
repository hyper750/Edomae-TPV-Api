from db.sqlalchemy.sqlalchemy import MA
from settings import MEAL_IMATGES_URL

from .file_serialization import FileSerialization


class MealSchema(MA.Schema):
    imatge = FileSerialization(upload_url=MEAL_IMATGES_URL, attribute="imatge")

    class Meta:
        fields = (
            "id",
            "enabled",
            "name",
            "category",
            "description",
            "price",
            "imatge",
            "order",
        )
