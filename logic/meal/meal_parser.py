from flask_restful import reqparse


def parse_object_meal() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('enabled', type=bool)
    parser = parser.add_argument('name', required=True, type=str)
    parser = parser.add_argument('description', type=str)
    parser = parser.add_argument('category', type=int)
    parser = parser.add_argument('price', required=True, type=float)
    parser = parser.add_argument('imatge', required=True, type=str)

    return parser.parse_args()


def parse_query_meal() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('enabled', type=bool, store_missing=False)
    parser = parser.add_argument('name', type=str, store_missing=False)
    parser = parser.add_argument('description', type=str, store_missing=False)
    parser = parser.add_argument('category', type=int, store_missing=False)
    parser = parser.add_argument('price', type=float, store_missing=False)
    parser = parser.add_argument('imatge', type=str, store_missing=False)

    return parser.parse_args()
