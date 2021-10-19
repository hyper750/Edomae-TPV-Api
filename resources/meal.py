from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models import Meal, MealSchema
from adapter.db import DB


class MealResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        meal = Meal.query.get(id=id)

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
        pass

    def post(self):
        pass
