from adapter.db import MA


class TableSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'number',
            'local',
            'x_coordinates',
            'y_coordinates',
        )
