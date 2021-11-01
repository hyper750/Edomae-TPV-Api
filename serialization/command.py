from adapter.db import MA


class CommandSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'user',
            'creation_date',
            'paid',
            'payment_method',
            'is_home_delivery',
            'delivery_address',
            'table',
            'table_name',
            'discount',
            'extra',
        )
