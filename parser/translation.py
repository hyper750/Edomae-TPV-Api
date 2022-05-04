from flask_restful import reqparse


def parse_translation_object():
    parser = reqparse.RequestParser()

    parser = parser.add_argument('key', type=str, required=True)
    parser = parser.add_argument('language', type=str, required=True)
    parser = parser.add_argument('value', type=str, required=True)

    return parser.parse_args()

def parser_translation_query():
    parser = reqparse.RequestParser()

    parser = parser.add_argument('key', type=str)
    parser = parser.add_argument('language', type=str)
    parser = parser.add_argument('value', type=str)

    return parser.parse_args()
