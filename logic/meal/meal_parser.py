from flask_restful import reqparse


def parse_object_meal() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('enabled', type=bool)
    parser = parser.add_argument('name', required=True, type=str)
    parser = parser.add_argument('price', required=True, type=float)
    parser = parser.add_argument('imatge_name', required=True, type=str)

    return parser.parse_args()


def parse_query_meal():
    pass
