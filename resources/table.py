from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import Table
from serialization import TableSchema


class TableResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        pass

    def put(self, id: int):
        pass

    def delete(self, id: int):
        pass


class TablesResources(Resource):
    method_decorators = (jwt_required(),)

    def post(self):
        pass

    def get(self):
        pass
