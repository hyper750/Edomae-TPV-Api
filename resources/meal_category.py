from parser import parse_object_meal_category, parse_query_meal_category

from db.sqlalchemy.sqlalchemy import DB
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
            return "", 404

        return MealCategorySchema().dump(category)

    def delete(self, id: int):
        category = MealCategory.query.get(id)

        meal_categories_to_shift = MealCategory.query.filter(
            MealCategory.order > category.order
        )

        for meal_category_to_shift in meal_categories_to_shift:
            meal_category_to_shift.order -= 1

        if category:
            category.delete()
        return "", 204

    def put(self, id: int):
        category = MealCategory.query.get(id)

        if not category:
            return "", 404

        params = parse_query_meal_category()

        # Increment/Decrement order
        if to_order := params.get("order"):
            current_order = category.order
            if current_order < to_order:
                categories_to_shift = MealCategory.query.filter(
                    MealCategory.order >= current_order + 1
                ).filter(MealCategory.order <= to_order)

                for category_to_shift in categories_to_shift:
                    category_to_shift.order -= 1
            else:
                categories_to_shift = MealCategory.query.filter(
                    MealCategory.order >= to_order
                ).filter(MealCategory.order <= current_order - 1)

                for category_to_shift in categories_to_shift:
                    category_to_shift.order += 1

        for key, value in params.items():
            setattr(category, key, value)

        category.save()

        return MealCategorySchema().dump(category)


class MealCategoriesResource(Resource):

    @jwt_required()
    def post(self):
        category = MealCategory(**parse_object_meal_category())

        # If order is not set, get the it from the last value
        if not category.order:
            last_order = DB.session.query(func.max(MealCategory.order)).scalar()
            next_order = 1
            if last_order:
                next_order = last_order + 1
            category.order = next_order

        category.save()

        return MealCategorySchema().dump(category), 201

    def get(self):
        categories = MealCategory.query.filter_by(
            **parse_query_meal_category()
        ).order_by(MealCategory.order, MealCategory.name)
        return MealCategorySchema(many=True).dump(categories)
