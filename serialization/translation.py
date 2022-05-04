from db.sqlalchemy.sqlalchemy import MA

from serialization import EnumSerialization


class TranslationSchema(MA.Schema):
    language = EnumSerialization(attribute='language')

    class Meta:
        fields = (
            'id',
            'key',
            'language',
            'value'
        )
