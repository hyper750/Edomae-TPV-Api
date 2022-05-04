from marshmallow.fields import Field


class EnumSerialization(Field):
    def _serialize(self, value, attr: str, obj, **kwargs):
        if value is None:
            return value

        return value.value
