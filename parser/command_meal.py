from flask_restful import reqparse


def parse_object_command_meal() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('command', type=int, required=True)
    parser = parser.add_argument('meal', type=int, required=True)
    parser = parser.add_argument('number', type=int, required=True)
    parser = parser.add_argument('extra', type=str)
    parser = parser.add_argument('discount', type=float)

    return parser.parse_args()


def parse_query_command_meal() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('command', type=int, store_missing=False)
    parser = parser.add_argument('meal', type=int, store_missing=False)
    parser = parser.add_argument('number', type=int, store_missing=False)
    parser = parser.add_argument('extra', type=str, store_missing=False)
    parser = parser.add_argument('discount', type=float, store_missing=False)

    return parser.parse_args()
