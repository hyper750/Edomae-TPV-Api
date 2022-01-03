from parser import parse_object_command_meal, parse_query_command_meal

from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import CommandMeal, Meal
from serialization import CommandMealSchema
from utils.math import calculate_discount

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
        command_meal_params = parse_object_command_meal()

        # Get meal
        meal = Meal.query.get(command_meal_params.get('meal'))
        # Add current price instance
        command_meal_params.price = meal.price
        # Compute total meal price from the discount (0-100)
        command_meal_params.total_price = calculate_discount(meal.price, command_meal_params.discount)

        command_meal = CommandMeal(
            **command_meal_params
        )

        command_meal.save()

        return CommandMealSchema().dump(command_meal), 201

    def get(self):
        command_meals = CommandMeal.query.filter_by(
            **parse_query_command_meal()
        )

        return CommandMealSchema(many=True).dump(command_meals)
