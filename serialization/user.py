from adapter.db import MA


class UserSchema(MA.Schema):
    class Meta:
        # Fields to serialize
        fields = (
            'id',
            'enabled',
            'username',
            'email',
            'admin'
        )
