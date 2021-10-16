from flask_jwt_extended import create_access_token
from flask_restful import Resource
from logic.user import authenticate_user, parse_login


class Auth(Resource):

    def post(self):
        parameters = parse_login()

        if user := authenticate_user(**parameters):
            token = create_access_token(user.id)
            return {
                'token': token
            }

        return {
            'error': 'User or password are not correct'
        }, 401

    def delete(self):
        return 'destroy jwt'
