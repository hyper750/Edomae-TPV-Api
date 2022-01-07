from parser import parse_object_meal_category, parse_query_meal_category

from adapter.db import DB
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import MealCategory
from serialization import MealCategorySchema
from sqlalchemy import func


class MealCategoryResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        category = MealCategory.query.get(id)

        if not category:
            return '', 404

        return MealCategorySchema().dump(category)

    def delete(self, id: int):
        category = MealCategory.query.get(id)
        if category:
            category.delete()
        return '', 204

    def put(self, id: int):
        category = MealCategory.query.get(id)

        if not category:
            return '', 404

        params = parse_query_meal_category()
        for key, value in params.items():
            setattr(category, key, value)

        category.save()

        return MealCategorySchema().dump(category)


class MealCategoriesResource(Resource):
    method_decorators = (jwt_required(),)

    def post(self):
        category = MealCategory(
            **parse_object_meal_category()
        )

        # If order is not set, get the it from the last value
        last_order = DB.session.query(func.max(MealCategory.order)).scalar()
        category.order = last_order + 1

        category.save()

        return MealCategorySchema().dump(category), 201

    def get(self):
        categories = MealCategory.query.filter_by(
            **parse_query_meal_category()
        ).order_by(MealCategory.order)
        return MealCategorySchema(many=True).dump(categories)
