from db.sqlalchemy.sqlalchemy import MA


class CommandMealSchema(MA.Schema):
    class Meta:
        fields = (
            "id",
            "command",
            "meal",
            "number",
            "extra",
            "discount",
            "price",
            "total_price",
        )
