from flask_restful import inputs, reqparse
from werkzeug.datastructures import FileStorage


def parse_object_meal() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('enabled', type=inputs.boolean)
    parser = parser.add_argument('name', required=True, type=str)
    parser = parser.add_argument('description', type=str)
    parser = parser.add_argument('category', type=int)
    parser = parser.add_argument('price', required=True, type=float)
    parser = parser.add_argument(
        'imatge', required=True, type=FileStorage, location='files'
    )
    parser = parser.add_argument('order', required=True, type=int)

    return parser.parse_args()


def parse_query_meal() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('enabled', type=inputs.boolean, store_missing=False)
    parser = parser.add_argument('name', type=str, store_missing=False)
    parser = parser.add_argument('description', type=str, store_missing=False)
    parser = parser.add_argument('category', type=int, store_missing=False)
    parser = parser.add_argument('price', type=float, store_missing=False)
    parser = parser.add_argument(
        'imatge', type=FileStorage, location='files', store_missing=False
    )
    parser = parser.add_argument('order', type=int, store_missing=False)

    return parser.parse_args()
