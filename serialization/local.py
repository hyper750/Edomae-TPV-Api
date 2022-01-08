from db.sqlalchemy.sqlalchemy import MA
from settings import LOCAL_IMATGES_URL

from .file_serialization import FileSerialization


class LocalSchema(MA.Schema):
    imatge = FileSerialization(upload_url=LOCAL_IMATGES_URL, attribute="imatge")

    class Meta:
        fields = (
            "id",
            "enabled",
            "name",
            "imatge",
        )
