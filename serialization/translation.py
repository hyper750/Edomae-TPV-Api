from db.sqlalchemy.sqlalchemy import MA


class TranslationSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'key',
            'language',
            'value'
        )
