from adapter.db import MA
from settings import MEAL_CATEGORY_URL

from .file_serialization import FileSerialization


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
