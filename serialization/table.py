from db.sqlalchemy.sqlalchemy import MA


class TableSchema(MA.Schema):
    class Meta:
        fields = (
            "id",
            "enabled",
            "number",
            "number_of_persons",
            "local",
            "x_coordinates",
            "y_coordinates",
        )
