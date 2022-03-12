from db.sqlalchemy.sqlalchemy import MA


class ContactMessageSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'creation_date',
            'is_reviewed',
            'name',
            'email',
            'message'
        )
