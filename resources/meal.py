from flask_jwt_extended import jwt_required
from flask_restful import Resource
from logic.meal import parse_object_meal, parse_query_meal
from models import Meal, MealSchema


class MealResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        meal = Meal.query.get(id)

        if not meal:
            return '', 404

        return MealSchema().dump(meal)

    def delete(self, id: int):
        meal = Meal.query.get(id)
        if meal:
            meal.delete()
        return '', 204

    def put(self, id: int):
        meal = Meal.query.get(id)

        if not meal:
            return '', 404

        params = parse_query_meal()
        for key, value in params.items():
            setattr(meal, key, value)

        meal.save()

        return MealSchema().dump(meal)


class MealsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        meals = Meal.query.filter_by(
            **parse_query_meal()
        )
        return MealSchema(many=True).dump(meals)

    def post(self):
        meal = Meal(
            **parse_object_meal()
        )
        meal.save()
        return MealSchema().dump(meal), 201
