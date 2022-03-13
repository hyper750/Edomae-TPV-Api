from flask_restful import inputs, reqparse


def parse_contact_message_query() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('page_size', type=int, default=50)
    parser = parser.add_argument('page_num', type=int, default=1)

    return parser.parse_args()


def parse_contact_message_object() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument('g-recaptcha-response', type=str, required=True)
    parser = parser.add_argument('name', type=str, required=True)
    parser = parser.add_argument('email', type=str, required=True)
    parser = parser.add_argument('message', type=str, required=True)

    return parser.parse_args()


def parse_contact_message_update() -> dict:
    parser = reqparse.RequestParser()

    parser = parser.add_argument(
        'is_reviewed', type=inputs.boolean, store_missing=False
    )

    return parser.parse_args()
