from flask_jwt_extended import create_access_token
from flask_restful import Resource
from logic.user import parse_login


class Auth(Resource):

    def post(self):
        parameters = parse_login()
        return 'create jwt'

    def delete(self):
        return 'destroy jwt'
