from parser import parse_object_meal, parse_query_meal

from db.sqlalchemy.sqlalchemy import DB
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import Meal
from serialization import MealSchema
from sqlalchemy import func


class MealResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        meal = Meal.query.get(id)

        if not meal:
            return "", 404

        return MealSchema().dump(meal)

    def delete(self, id: int):
        meal = Meal.query.get(id)

        meals_to_shift = Meal.query.filter(Meal.order > meal.order)
        for meal_to_shift in meals_to_shift:
            meal_to_shift.order -= 1

        if meal:
            meal.delete()
        return "", 204

    def put(self, id: int):
        meal = Meal.query.get(id)

        if not meal:
            return "", 404

        params = parse_query_meal()

        # Shift other items order
        if to_order := params.get("order"):
            current_order = meal.order
            if current_order < to_order:
                meals_to_shift = Meal.query.filter(
                    Meal.order >= current_order + 1
                ).filter(Meal.order <= to_order)

                for meal_to_shift in meals_to_shift:
                    meal_to_shift.order -= 1
            else:
                meals_to_shift = Meal.query.filter(Meal.order >= to_order).filter(
                    Meal.order <= current_order - 1
                )

                for meal_to_shift in meals_to_shift:
                    meal_to_shift.order += 1

        for key, value in params.items():
            setattr(meal, key, value)

        meal.save()

        return MealSchema().dump(meal)


class MealsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        meals = Meal.query.filter_by(**parse_query_meal()).order_by(Meal.order)
        return MealSchema(many=True).dump(meals)

    def post(self):
        params = parse_object_meal()
        meal = Meal(**params)

        # Dynamically add the order
        if not meal.order:
            last_order = (
                DB.session.query(func.max(Meal.order))
                .filter(Meal.category == meal.category)
                .scalar()
            )
            next_order = 1
            if last_order:
                next_order = last_order + 1
            meal.order = next_order

        meal.save()

        return MealSchema().dump(meal), 201
