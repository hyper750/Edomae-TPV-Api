from flask_restful import reqparse
from werkzeug.datastructures import FileStorage


def parse_object_meal_category() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('name', required=True, type=str)
    parser = parser.add_argument(
        'imatge', type=FileStorage, location='files', required=True
    )

    return parser.parse_args()


def parse_query_meal_category() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('name', type=str, store_missing=False)
    parser = parser.add_argument(
        'imatge', type=FileStorage, location='files', store_missing=False
    )

    return parser.parse_args()
