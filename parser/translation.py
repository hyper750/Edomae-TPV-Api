from flask_restful import reqparse


def parse_translation_object() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('key', type=str, required=True)
    parser = parser.add_argument('language', type=str, required=True)
    parser = parser.add_argument('value', type=str, required=True)

    return parser.parse_args()

def parse_translation_query() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('key', type=str)
    parser = parser.add_argument('language', type=str)
    parser = parser.add_argument('value', type=str)

    return parser.parse_args()
