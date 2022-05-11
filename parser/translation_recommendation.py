from flask_restful import inputs, reqparse


def parse_translation_recommendation_query() -> dict:
    parser = reqparse.RequestParser()

    parser.add_argument('enabled', type=inputs.boolean, store_missing=False)

    return parser.parse_args()
