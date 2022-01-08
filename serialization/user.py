from db.sqlalchemy.sqlalchemy import MA


class UserSchema(MA.Schema):
    class Meta:
        # Fields to serialize
        fields = (
            "id",
            "enabled",
            "username",
            "email",
            "admin",
            "name",
            "surname",
            "lastname",
        )
