from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from flask_restful import Resource
from logic.user import authenticate_user, parse_login, revoke_access_token


class Auth(Resource):

    def post(self):
        parameters = parse_login()

        if user := authenticate_user(**parameters):
            token = create_access_token(user.id)
            return {
                'token': token
            }

        return {
            'msg': 'User or password are not correct'
        }, 401

    @jwt_required()
    def delete(self):
        jti = get_jwt()['jti']
        revoke_access_token(jti)
        return {
            'msg': 'Access token revoked'
        }
