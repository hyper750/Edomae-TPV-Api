from adapter.db import DB
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from logic.meal_category import (
    parse_object_meal_category,
    parse_query_meal_category
)
from models import MealCategory, MealSchema
from models.meal_category import MealCategorySchema


class MealCategoryResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        category = MealCategory.query.get(id)

        if not category:
            return '', 404

        return MealSchema().dump(category)

    def delete(self, id: int):
        MealCategory.query.filter_by(id=id).delete()
        return '', 204

    def put(self, id: int):
        category = MealCategory.query.get(id)

        if not category:
            return '', 404

        params = parse_query_meal_category()
        for key, value in params.items():
            setattr(category, key, value)

        DB.session.commit()

        return MealCategorySchema().dump(category)


class MealCategoriesResource(Resource):
    method_decorators = (jwt_required(),)

    def post(self):
        category = MealCategory(
            **parse_object_meal_category()
        )

        DB.session.add(category)
        DB.session.commit()

        return MealCategorySchema().dump(category), 201

    def get(self):
        categories = MealCategory.query.filter_by(
            **parse_query_meal_category()
        )
        return MealCategorySchema(many=True).dump(categories)
