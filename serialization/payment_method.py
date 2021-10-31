from adapter.db import MA


class PaymentMethodSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'enabled',
            'name'
        )
