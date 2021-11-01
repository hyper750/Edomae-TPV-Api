from flask_restful import reqparse


def parse_login():
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, type=str)
    parser.add_argument('password', required=True, type=str)
    return parser.parse_args()
