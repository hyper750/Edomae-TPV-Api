from parser import parse_object_command_meal, parse_query_command_meal

from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import CommandMeal
from serialization import CommandMealSchema


class CommandMealResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        command_meal = CommandMeal.query.get(id)

        if not command_meal:
            return '', 404

        return CommandMealSchema().dump(command_meal)

    def put(self, id: int):
        command_meal = CommandMeal.query.get(id)

        if not command_meal:
            return '', 404

        for key, value in parse_query_command_meal().items():
            setattr(command_meal, key, value)

        command_meal.save()

        return CommandMealSchema().dump(command_meal)

    def delete(self, id: int):
        command_meal = CommandMeal.query.get(id)

        if command_meal:
            command_meal.delete()

        return '', 204


class CommandMealsResource(Resource):
    method_decorators = (jwt_required(),)

    def post(self):
        command_meal = CommandMeal(
            **parse_object_command_meal()
        )

        command_meal.save()

        return CommandMealSchema().dump(command_meal), 201

    def get(self):
        command_meals = CommandMeal.query.filter_by(
            **parse_query_command_meal()
        )

        return CommandMealSchema(many=True).dump(command_meals)
