from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from models import User
from serialization import UserSchema


class User(Resource):
    method_decorators = (jwt_required(),)

    # TODO: Admin can modify users, for example disable a user
    # TODO: Admin can delete users
    # TODO: Admin can access other user info, displaying all the users for example

    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        return UserSchema().dump(user)
