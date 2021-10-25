from flask import request
from marshmallow.fields import Field


class FileSerialization(Field):
    def __init__(self, upload_url: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.upload_url = upload_url

    def _serialize(self, value, attr: str, obj, **kwargs):
        if value is None:
            return value

        return f'{request.host_url}{self.upload_url}/{value}'
