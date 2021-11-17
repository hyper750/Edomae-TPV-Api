from flask_restful import inputs, reqparse


def parse_object_payment_method() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('enabled', type=inputs.boolean)
    parser = parser.add_argument('name', required=True, type=str)

    return parser.parse_args()


def parse_query_payment_method() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('enabled', type=inputs.boolean, store_missing=False)
    parser = parser.add_argument('name', type=str, store_missing=False)

    return parser.parse_args()
