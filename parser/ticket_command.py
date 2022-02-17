from flask_restful import reqparse, inputs


def parse_query_ticket_command() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('creation_date__gte', type=inputs.datetime_from_iso8601, required=True)
    parser = parser.add_argument('creation_date__lte', type=inputs.datetime_from_iso8601, required=True)

    return parser.parse_args()