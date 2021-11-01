from parser import parse_object_command_meal, parse_query_command_meal

from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import CommandMeal
from serialization import CommandMealSchema


class CommandMealResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        pass

    def put(self, id: int):
        pass

    def delete(self, id: int):
        pass


class CommandMealsResource(Resource):
    method_decorators = (jwt_required(),)

    def post(self):
        pass

    def get(self):
        pass
