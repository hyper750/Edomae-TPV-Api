from flask_restful import inputs, reqparse


def parse_object_table() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('enabled', type=inputs.boolean)
    parser = parser.add_argument('number', type=int, required=True)
    parser = parser.add_argument('local', type=int, required=True)
    parser = parser.add_argument('number_of_persons', type=int, required=True)
    parser = parser.add_argument('x_coordinates', type=float, required=True)
    parser = parser.add_argument('y_coordinates', type=float, required=True)

    return parser.parse_args()


def parse_query_table() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument(
        'enabled', type=inputs.boolean, store_missing=False
    )
    parser = parser.add_argument('number', type=int, store_missing=False)
    parser = parser.add_argument('local', type=int, store_missing=False)
    parser = parser.add_argument(
        'number_of_persons', type=int, store_missing=False
    )
    parser = parser.add_argument(
        'x_coordinates', type=float, store_missing=False
    )
    parser = parser.add_argument(
        'y_coordinates', type=float, store_missing=False
    )

    return parser.parse_args()
