from flask_restful import reqparse


def parse_object_command() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('paid', type=bool, store_missing=False)
    parser = parser.add_argument('payment_method', type=int, store_missing=False)

    return parser.parse_args()


def parse_query_command() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('user', type=int, store_missing=False)
    parser = parser.add_argument('paid', type=bool, store_missing=False)
    parser = parser.add_argument('payment_method', type=int, store_missing=False)
    parser = parser.add_argument('page_size', type=int, default=50)
    parser = parser.add_argument('page_num', type=int, default=1)

    return parser.parse_args()
