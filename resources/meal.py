from adapter.db import DB
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from logic.meal import parse_object_meal
from models import Meal, MealSchema


class MealResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        meal = Meal.query.get(id)

        if not meal:
            return '', 404

        return MealSchema().dump(meal)

    def delete(self, id: int):
        Meal.query.filter_by(id=id).delete()
        DB.session.commit()
        return '', 204

    def put(self, id: int):
        pass


class MealsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        meals = Meal.query.filter_by()
        return MealSchema(many=True).dump(meals)

    def post(self):
        meal = Meal(
            **parse_object_meal()
        )
        DB.session.add(meal)
        DB.session.commit()

        return MealSchema().dump(meal), 201
