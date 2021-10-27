from flask_restful import reqparse, inputs


def parse_object_command() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('paid', type=bool, store_missing=False)
    parser = parser.add_argument('payment_method', type=int, store_missing=False)
    parser = parser.add_argument('is_home_delivery', type=bool, store_missing=False)
    parser = parser.add_argument('delivery_address', type=str, store_missing=False)

    return parser.parse_args()


def parse_query_command() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('page_size', type=int, default=50)
    parser = parser.add_argument('page_num', type=int, default=1)

    parser = parser.add_argument('creation_date__gte', type=inputs.datetime_from_iso8601, store_missing=False)
    parser = parser.add_argument('creation_date__lte', type=inputs.datetime_from_iso8601, store_missing=False)
    parser = parser.add_argument('user', type=int, store_missing=False)
    parser = parser.add_argument('paid', type=bool, store_missing=False)
    parser = parser.add_argument('payment_method', type=int, store_missing=False)
    parser = parser.add_argument('is_home_delivery', type=bool, store_missing=False)
    parser = parser.add_argument('delivery_address', type=str, store_missing=False)

    return parser.parse_args()
