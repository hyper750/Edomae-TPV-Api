from flask_restful import reqparse


def parse_object_meal_category() -> dict:
    parser = reqparse.RequestParser()
    
    parser = parser.add_argument('name', required=True, type=str)
    parser = parser.add_argument('imatge_name', required=True, type=str)

    return parser.parse_args()


def parse_query_meal_category() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('name', type=str, store_missing=False)
    parser = parser.add_argument('imatge_name', type=str, store_missing=False)

    return parser.parse_args()
