from adapter.db import MA
from settings import PAYMENT_METHOD_IMATGES_URL

from .file_serialization import FileSerialization


class PaymentMethodSchema(MA.Schema):
    image = FileSerialization(
        upload_url=PAYMENT_METHOD_IMATGES_URL,
        attribute='image'
    )

    class Meta:
        fields = (
            'id',
            'enabled',
            'name',
            'image'
        )
