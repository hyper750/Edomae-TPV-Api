from flask_restful import inputs, reqparse


def parse_object_command() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('paid', type=inputs.boolean, store_missing=False)
    parser = parser.add_argument('payment_method', type=int, store_missing=False)
    parser = parser.add_argument('is_home_delivery', type=inputs.boolean, store_missing=False)
    parser = parser.add_argument('delivery_address', type=str, store_missing=False)
    parser = parser.add_argument('delivery_details', type=str, store_missing=False)
    parser = parser.add_argument('extra', type=str, store_missing=False)
    parser = parser.add_argument('discount', type=float, store_missing=False)
    parser = parser.add_argument('table', type=int, store_missing=False)
    parser = parser.add_argument('table_name', type=str, store_missing=False)


    return parser.parse_args()


def parse_query_command() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('page_size', type=int, default=50)
    parser = parser.add_argument('page_num', type=int, default=1)

    parser = parser.add_argument('creation_date__gte', type=inputs.datetime_from_iso8601, store_missing=False)
    parser = parser.add_argument('creation_date__lte', type=inputs.datetime_from_iso8601, store_missing=False)

    parser = parser.add_argument('user', type=int, store_missing=False)

    parser = parser.add_argument('paid', type=inputs.boolean, store_missing=False)
    parser = parser.add_argument('payment_method', type=int, store_missing=False)

    parser = parser.add_argument('is_home_delivery', type=inputs.boolean, store_missing=False)
    parser = parser.add_argument('delivery_address', type=str, store_missing=False)
    parser = parser.add_argument('table', type=int, store_missing=False)
    parser = parser.add_argument('table_name', type=str, store_missing=False)

    parser = parser.add_argument('discount', type=float, store_missing=False)

    return parser.parse_args()
