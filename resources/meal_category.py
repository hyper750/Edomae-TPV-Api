from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import MealCategory, MealSchema


class MealCategoryResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        category = MealCategory.query.get(id)

        if not category:
            return '', 404

        return MealSchema().dump(category)

    def delete(self, id: int):
        MealCategory.query_filter_by(id=id).delete()
        return '', 204

    def put(self, id: int):
        pass


class MealCategoriesResource(Resource):
    method_decorators = (jwt_required(),)

    def post(self):
        pass

    def get(self):
        pass
